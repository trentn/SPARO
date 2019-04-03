#!/usr/bin/env python

#if moving in phi while trying to move in the x and y there will have to
#sufficiently high communication rate between the RPi and Arduino. This is the major
#limiting factor in this type of movement.

from speed2RPM import speed2RPM #decodes desired xyphi to motor commands
import threading
import serial
import time
import numpy as np
import math 

from system_state.msg import *
import rospy

pub = rospy.Publisher("at_location", AtLocation, queue_size=1)

#eventually this program will send encoder data up to the localization
#hub and receive its predicted current_location from said hub.
#This program will recieve desired locations from the higher level mission files
#Eventually, this will just be the manager between the desired_location
#and the motor commands needed to get there.

print "program started"

error_threshold = np.matrix([[.01],[.01],[1.0/180.0*math.pi]]) #How close we try to get to final position

at_location = False

outer_d = .4570
wheel_d = .1524 #wheel diameter in meters (6")
wheel_dist_per_rev = wheel_d*math.pi

current_location = np.matrix([[0.0],[0.0],[0.0]]) #x(m) y(m) phi(rad) since program start
desired_location = np.matrix([[0.0],[0.0],[0.0]]) #same formatting as current_location
catchSpeeds = True
sendSpeeds = True

dx = 0.0
dy = 0.0
dphi = 0.0

loc_log = open("location.log", 'w', buffering=1)
ang_vel_log = open("desired_vel.log", 'w', buffering=1)

position_error = np.matrix(np.zeros((4,3))) #x/y/phi/time,timestep
RPM_history = np.matrix(np.zeros((5,3))) #m1/m2/m3/m4/time,timestep

kinematics_matrix = np.matrix([[1.0,0.,outer_d/2],[0.,1.,outer_d/2.],[-1.,0.,outer_d/2.],[0.,-1.,outer_d/2.]])/wheel_dist_per_rev*60
inv_kinematics_matrix = np.linalg.pinv(kinematics_matrix)

xy_gains = np.matrix([[1],[0.]]) #kp,kd no forseeable reason for x and y to have seperate gains
phi_gains = np.matrix([[.5],[0.]]) #kp,kd for phi
send_rate = .05 #rate of data transfer to arduino. used in send_Arduino thread
catch_rate = .05 #rate the Arduino should send to the RPi

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flush()

print "Serial initialized"

def initialize_Arduino(): #intention is for function to run serial setup and send any parameters we want to arduino, for now only message frequency, maybe later different modes.
    print "initialize_Arduino entered"
    ser.write("Are you ready kids?,"+str(catch_rate)+"\n") #so far catch rate is the only thing this is concerned with but later we can add additional things to make arduino updates easier on the fly
    print "Message sent"
    initalize_response = ser.readline()
    print "Read line captured"
    if repr(initalize_response) == repr("Aye aye captain!\r\n"):
        print "Response received"
        sendSpeeds = True
        catchSpeeds = True
       #print str(sendSpeeds) + " " + str(catchSpeeds)
        time.sleep(2)
    else:
        print "Unexpected response " + repr(initalize_response) + initalize_response
    return

def position_PID(): #desired xyphi speeds from the absolute frame determined here
    check_Error()
    #pushes back position error history
    for i in range(4):
        for j in reversed(range(1,3)):
            position_error[i,j] = position_error[i,j-1]

    position_error[0:3,0] = desired_location - current_location #updating error. will need to capture multiple timesteps for non proportional control

    position_error[3,0] = RPM_history[4,0] #runs off of RPi time in seconds

    #currently just proportional controller. setting other gains is useless before I have a chance to tune
    dx_abs = xy_gains[0]*position_error[0,0]
    dy_abs = xy_gains[0]*position_error[1,0]
    dphi_abs = phi_gains[0]*position_error[2,0]


    [dx,dy,dphi] = absolute2Local(dx_abs,dy_abs,dphi_abs)
    ang_vel_log.write(str(dx) + "," +str(dy)+","+str(dphi)+"\n")

    return [dx,dy,dphi]

def check_Error():
    #rospy.loginfo("checking error")
    #rospy.loginfo(str(abs(position_error[2,0]))+"<"+str(error_threshold[2,0])+"="+str(abs(position_error[2,0]) < error_threshold[2,0]))
    if( abs(position_error[0,0]) < error_threshold[0,0] and abs(position_error[1,0]) < error_threshold[1,0] and abs(position_error[2,0]) < error_threshold[2,0] ):
        at_location = True
        try:
            pub.publish(AtLocation(True))
        except Exception:
            pass
    else:
        at_location = False
        try:
            pub.publish(AtLocation(False))
        except Exception:
            pass   
    return

def send_Arduino(): #sends commands to arduino at a consitant rate
    slog = open("send.log", 'w', buffering=1)
    global position_error
    global dx
    global dy
    global dphi
    global sendSpeeds

    while(sendSpeeds == True):
        [dx,dy,dphi] = position_PID()
        [m1,m2,m3,m4,scale_factor] = speed2RPM(dx,dy,dphi)
        ang_vel_log.write(str(dx) + "," +str(dy)+","+str(dphi)+"\n")
        m1 = float(m1)
        m2 = float(m2)
        m3 = float(m3)
        m4 = float(m4)
    
        ser.write(str(m1)+","+str(m2)+","+str(m3)+","+str(m4)+"\n")
        slog.write(str(m1)+","+str(m2)+","+str(m3)+","+str(m4)+"\n")
       
        #enter in scale_factor check --- not sure if this is important yet
        time.sleep(send_rate)

    return

def catch_Arduino(): #thread function to catch arduino updates from serial
    
    global position_error
    global dx
    global dy
    global dphi
    global current_location
    global RPM_history
    global desired_location
    global catchSpeeds

    rlog = open("receive.log", 'w', buffering=1)

    while(catchSpeeds == True):
        arduino_in = ser.readline() #formatting ("m1,m2,m3,m4,arduino_time")
        arduino_in.decode('latin-1')
        rlog.write(arduino_in)
        input_vector = arduino_in.split(",")
        if(len(input_vector) == 5):

            for i in range(5):
                for j in reversed(range(1,3)):
                    RPM_history[i,j] = RPM_history[i,j-1]
                RPM_history[i,0] = float(input_vector[i])

            temp_speed_local = inv_kinematics_matrix*RPM_history[0:4,:]
            temp_speed_abs = np.matrix([[math.cos(-current_location[2,0]),-math.sin(-current_location[2,0]),0],[math.sin(-current_location[2,0]),math.cos(-current_location[2,0]),0],[0,0,1]])*temp_speed_local
            current_location[:,0] = current_location[:,0] - .5*(temp_speed_abs[:,0]+temp_speed_abs[:,1])*(RPM_history[4,1]-RPM_history[4,0])
        else:
            print(input_vector)

        loc_log.write(str(float(current_location[0,0]))+",")
        loc_log.write(str(float(current_location[1,0]))+",")
        loc_log.write(str(float(current_location[2,0]))+",")
        loc_log.write(str(float(desired_location[0,0]))+",")
        loc_log.write(str(float(desired_location[1,0]))+",")
        loc_log.write(str(float(desired_location[2,0]))+",")
        loc_log.write(str(float(position_error[0,0]))+",")
        loc_log.write(str(float(position_error[1,0]))+",")
        loc_log.write(str(float(position_error[2,0]))+",")
        loc_log.write(str(position_error[3,0])+"\n")


    return

def absolute2Local(dx_abs,dy_abs,dphi_abs): #takes in absolute reference velocities and decodes to robot frame and updates the global values
    dphi = dphi_abs
    dx = dx_abs*math.cos(current_location[2,0])-dy_abs*math.sin(current_location[2,0])
    dy = dx_abs*math.sin(current_location[2,0])+dy_abs*math.cos(current_location[2,0])
    
    dphi = float(dphi)
    dx = float(dx)
    dy = float(dy)

    return [dx,dy,dphi]

def handle_move_robot(des_loc):
    desired_location[0,0] = float(des_loc.X)
    desired_location[1,0] = float(des_loc.Y)
    desired_location[2,0] = float(des_loc.phi)

    rospy.loginfo("X:%f Y:%f PHI:%f" %(des_loc.X, des_loc.Y, des_loc.phi))

def locomotion_node():
    rospy.init_node("locomotion")
    rospy.loginfo("Locomotion system is running")
    s = rospy.Subscriber("move_commands", MoveCommand, handle_move_robot)
    rospy.spin()

if __name__ == "__main__":
    
    initialize_Arduino()
    arduino_catch = threading.Thread(target=catch_Arduino, args=())
    arduino_send =threading.Thread(target=send_Arduino, args=())
    arduino_catch.start()
    arduino_send.start()

    locomotion_node()

    sendSpeeds = False
    catchSpeeds = False
    arduino_catch.join()
    arduino_send.join()
    ser.write("-999,0,0,0\n") #sending reset protocol to arduino
