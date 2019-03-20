#!/usr/bin/env python

#NOTE!!! if moving in phi while trying to move in the x and y there will have to
#sufficiently high communication rate between the RPi and Arduino. This is the major
#limiting factor in this type of movement.

from speed2RPM import speed2RPM #decodes desired xyphi to motor commands
import threading
import serial
import time
import numpy as np

#eventually this program will send encoder data up to the localization
#hub and receive its predicted current_location from said hub.
#This program will recieve desired locations from the higher level mission files
#Eventually, this will just be the manager between the desired_location
#and the motor commands needed to get there.

current_location = np.matrix([0,0,0]) #x(m) y(m) phi(rad) since program start
desired_location = np.matrix([0,0,0]) #same formatting as current_location
catchSpeeds = True
sendSpeeds = True

dx = 0;
dy = 0;
dphi = 0;

position_error = np.zeros(4,3) #x/y/phi/time,timestep
RPM_history = np.zeros(5,3) #m1/m2/m3/m4/time,timestep

kinematics_matrix = np.matrix([-1,0,outer_d/2],[0,-1,outer_d/2],[1,0,outer_d/2],[0,1,outer_d/2])/wheel_dist_per_rev*60
inv_kinematics_matrix = np.pinv(kinematics_matrix)

xy_gains = np.array([0,0]) #kp,kd no forseeable reason for x and y to have seperate gains
phi_gains = np.array([0,0]) #kp,kd for phi
send_rate = .01 #rate of data transfer to arduino. used in send_Arduino thread
catch_rate = .01 #rate the Arduino should send to the RPi

ser = serial.Serial("/dev/ttyACM0", 9600)

initalize_Arduino()

arduino_catch = threading.Thread(target=catch_Arduino, args=())
arduino_send =threading.Thread(target=send_Arduino, args=())

arduino_catch.start()
arduino_send.start()

while True: #main program loop
    location_string = raw_input("Enter desired location: ")
    #possibly check for a reset command/closeout command etc...
    desired_location = float(split(location_string))


sendSpeeds = False
catchSpeeds = False
arduino_catch.join()
arduino_send.join()

#eventually can move these functions to their own .py files.

def send_Arduino(): #sends commands to arduino at a consitant rate
    while(sendSpeeds == True):
        position_PID()
        [m1,m2,m3,m4,scale_factor] = speed2RPM(dx,dy,dphi)
        #enter in scale_factor check --- not sure if this is important yet
        ser.write(m1+","+m2+','+m3+','+m4+"\n")
        wait(send_rate)
    return

def initalize_Arduino(): #intention is for function to run serial setup and send any parameters we want to arduino, for now only message frequency, maybe later different modes.
        ser.write(catch_rate+"\n") #so far catch rate is the only thing this is concerned with but later we can add additional things to make arduino updates easier on the fly
    return

def position_PID(): #desired xyphi speeds from the absolute frame determined here


    #pushes back position error history
    for i in range(1,4):
        for j in reversed(range(3)):
            position_error(j,i) = position_error(j,i-1)

    for i in range(3):
        position_error(i,0) = desired_location(i) - current_location(i) #updating error. will need to capture multiple timesteps for non proportional control

    position_error(3,0) = time.clock() #runs off of RPi time in seconds

    #currently just proportional controller. setting other gains is useless before I have a chance to tune
    dx_abs = xy_gains(0)*position_error(0)
    dy_abs = xy_gains(0)*position_error(1)
    dphi_abs = phi_gains(0)*position_error(2)
    absolute2Local(dx_abs,dy_abs,dphi_abs)
    return

def catch_Arduino(): #thread function to catch arduino updates from serial
    while(catchSpeeds == true):
        arduino_in = ser.readline() #formatting ("m1,m2,m3,m4,arduino_time")
        input_vector = float(split(arduino_in.split(","))

        for i in range(5):
            for j in reversed(range(1,3)):
                RPM_history(i,j) = RPM_history(i,j-1)
            RPM_history(i,0) = input_vector(i)
        #decode into current absolute speed and take current location using trapezoid integration
        temp_speed_local = inv_kinematics_matrix*RPM_history(0:3,:)
        temp_speed_abs = np.matrix([cos(-current_location(2)),-sin(-current_location(2)),0],[sin(-current_location(2)),cos(-current_location(2)),0],[0,0,1])*temp_speed_local
        current_location = current_location + .5*(temp_speed_abs(:,0)+temp_speed_abs(:,1))*(RPM_history(4,1)-RPM_history(4,0))
    return

def absolute2Local(dx_abs,dy_abs,dphi_abs): #takes in absolute reference velocities and decodes to robot frame and updates the global values
    dphi = dphi_abs
    dx = dx_abs*cos(current_location(2))-dy_abs*sin(current_location(2))
    dy = dx_abs*sin(current_location(2))+dy_abs*cos(current_location(2))
    return
