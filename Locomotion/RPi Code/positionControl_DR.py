#!/usr/bin/env python

#NOTE!!! if moving in phi while trying to move in the x and y there will have to
#sufficiently high communication rate between the RPi and Arduino. This is the major
#limiting factor in this type of movement.

from speed2RPM import speed2RPM #decodes desired xyphi to motor commands
import threading
import serial
import time
import numpy as np
import math 

#eventually this program will send encoder data up to the localization
#hub and receive its predicted current_location from said hub.
#This program will recieve desired locations from the higher level mission files
#Eventually, this will just be the manager between the desired_location
#and the motor commands needed to get there.

print "program started"

outer_d = .6096
wheel_d = .1524 #wheel diameter in meters (6")
wheel_dist_per_rev = wheel_d*math.pi

current_location = np.matrix([[0],[0],[0]]) #x(m) y(m) phi(rad) since program start
desired_location = np.matrix([[0],[0],[0]]) #same formatting as current_location
catchSpeeds = True
sendSpeeds = True

dx = 0
dy = 0
dphi = 0

position_error = np.matrix(np.zeros((4,3))) #x/y/phi/time,timestep
RPM_history = np.matrix(np.zeros((5,3))) #m1/m2/m3/m4/time,timestep

kinematics_matrix = np.matrix([[-1,0,outer_d/2],[0,-1,outer_d/2],[1,0,outer_d/2],[0,1,outer_d/2]])/wheel_dist_per_rev*60
inv_kinematics_matrix = np.linalg.pinv(kinematics_matrix)

xy_gains = np.matrix([[0],[0]]) #kp,kd no forseeable reason for x and y to have seperate gains
phi_gains = np.matrix([[0],[0]]) #kp,kd for phi
send_rate = 1 #rate of data transfer to arduino. used in send_Arduino thread
catch_rate = 1 #rate the Arduino should send to the RPi

ser = serial.Serial("/dev/ttyACM0", 9600)
print "Serial initialized"

def initialize_Arduino(): #intention is for function to run serial setup and send any parameters we want to arduino, for now only message frequency, maybe later different modes.
    print "initialize_Arduino entered"
    ser.write("Are you ready kids?,"+str(catch_rate)+"\n") #so far catch rate is the only thing this is concerned with but later we can add additional things to make arduino updates easier on the fly
    initalize_response = ser.readline()
    print "Read line captured"
    if repr(initalize_response) == repr("Aye aye captain!\r\n"):
        print "Response received"
        sendSpeeds = True
        catchSpeeds = True
        print str(sendSpeeds) + " " + str(catchSpeeds)
        time.sleep(2)
    else:
        print "Unexpected response " + repr(initalize_response) + initalize_response
    return

def position_PID(): #desired xyphi speeds from the absolute frame determined here


    #pushes back position error history
    for i in range(1,4):
        for j in reversed(range(3)):
            position_error[i,j] = position_error[i,j-1]

    position_error[0:3] = desired_location - current_location #updating error. will need to capture multiple timesteps for non proportional control

    position_error[3] = time.clock() #runs off of RPi time in seconds

    #currently just proportional controller. setting other gains is useless before I have a chance to tune
    dx_abs = xy_gains[0]*position_error[0,0]
    dy_abs = xy_gains[0]*position_error[0,1]
    dphi_abs = phi_gains[0]*position_error[0,2]
    absolute2Local(dx_abs,dy_abs,dphi_abs)
    return

def send_Arduino(): #sends commands to arduino at a consitant rate
    print "In send thread " + str(sendSpeeds)
    while(sendSpeeds == True):
        print "Send loop"
        position_PID()
        [m1,m2,m3,m4,scale_factor] = speed2RPM(dx,dy,dphi)
        print "Sending to arduino " + str(m1)+","+str(m2)+","+str(m3)+","+str(m4)
        #enter in scale_factor check --- not sure if this is important yet
        ser.write(str(m1)+","+str(m2)+","+str(m3)+","+str(m4)+"\n")
        time.sleep(send_rate)

    return


def catch_Arduino(): #thread function to catch arduino updates from serial
    print "In catch thread " + str(catchSpeeds)
    while(catchSpeeds == True):
        print "catch loop"
        arduino_in = ser.readline() #formatting ("m1,m2,m3,m4,arduino_time")
        print arduino_in
        input_vector = arduino_in.split(",")
        #print len(input_vector)
        for i in range(5):
            for j in reversed(range(1,3)):

                RPM_history[i,j] = RPM_history[i,j-1]
            RPM_history[i,0] = float(input_vector[i])
        #decode into current absolute speed and take current location using trapezoid integration
        temp_speed_local = inv_kinematics_matrix*RPM_history[0:4,:]
        temp_speed_abs = np.matrix([[math.cos(-current_location[2]),-math.sin(-current_location[2]),0],[math.sin(-current_location[2]),math.cos(-current_location[2]),0],[0,0,1]])*temp_speed_local
        current_location[:] = current_location[:] + .5*(temp_speed_abs[:,0]+temp_speed_abs[:,1])*(RPM_history[4,1]-RPM_history[4,0])
    return

def absolute2Local(dx_abs,dy_abs,dphi_abs): #takes in absolute reference velocities and decodes to robot frame and updates the global values
    dphi = dphi_abs
    dx = dx_abs*math.cos(current_location[2])-dy_abs*math.sin(current_location[2])
    dy = dx_abs*math.sin(current_location[2])+dy_abs*math.cos(current_location[2])
    return


initialize_Arduino()



arduino_catch = threading.Thread(target=catch_Arduino, args=())
arduino_send =threading.Thread(target=send_Arduino, args=())

arduino_catch.start()
arduino_send.start()

while True: #main program loop
    location_string = raw_input("Enter desired location: ")
    #possibly check for a reset command/closeout command etc...
    locations = location_string.split(',')
    desired_location[0] = float(locations[0])
    desired_location[1] = float(locations[1])
    desired_location[2] = float(locations[2])
    print desired_location[0]
    if desired_location[0] == -999:
        break



sendSpeeds = False
catchSpeeds = False
arduino_catch.join()
arduino_send.join()

#eventually can move these functions to their own .py files.
