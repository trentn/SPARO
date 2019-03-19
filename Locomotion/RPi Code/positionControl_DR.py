#!/usr/bin/env python

#NOTE!!! if moving in phi while trying to move in the x and y there will have to
#sufficiently high communication rate between the RPi and Arduino. This is the major
#limiting factor in this type of movement.

from speed2RPM import speed2RPM #decodes desired xyphi to motor commands
import threading
import serial
import time
import numpy

current_location = numpy.array([0,0,0]) #x(m) y(m) phi(rad) since program start
desired_location = numpy.array([0,0,0]) #same formatting as current_location
catchSpeeds = true
sendSpeeds = true

dx = 0;
dy = 0;
dphi = 0;

xy_gains = numpy.array([0,0]) #kp,kd no forseeable reason for x and y to have seperate gains
phi_gains = numpy.array([0,0]) #kp,kd for phi
send_rate = .01 #rate of data transfer to arduino. used in send_Arduino thread
catch_rate = .01 #rate the Arduino should send to the RPi

initalize_Arduino()



#insert ability to take user input through ssh for position control
arduino_catch = threading.Thread(target=catch_Arduino, args=())
arduino_send =threading.Thread(target=send_Arduino, args=())

arduino_catch.start()
arduino_send.start()

while(true): #main program loop
    #insert stuff here
    #eventually this will be checking external things but for now it will
    #take commands from terminal



sendSpeeds = false
catchSpeeds = false
arduino_catch.join()
arduino_send.join()

#now that I think about it, if we are closing the loop we can do syncronous
#communication and have no need for threading but this would allow us to not
#worry about asynchronous timing issues

#eventually can move these functions to their own .py files.

def send_Arduino(): #sends commands to arduino at a consitant rate
    while(sendSpeeds == true):
        #position_PID can be done here, as it only needs to be updated when
        #updating the arduino
    return

def initalize_Arduino(): #intention is for function to run serial setup and send any parameters we want to arduino, for now only message frequency, maybe later different modes.

#setup serial connection

#send arduino command that it is waiting for in startup mode, setting time
#parameter etc... this allows for us to update various arduino parameters later on
#without changing base arduino code in the start up command parsing


    return

def position_PID(): #desired xyphi speeds from the absolute frame determined here

    position_error = desired_location - current_location

    #currently just proportional controller. setting other gains is useless before I have a chance to tune
    dx_abs = xy_gains(0)*position_error(0)
    dy_abs = xy_gains(0)*position_error(1)
    dphi_abs = phi_gains(0)*position_error(2)

    return

def catch_Arduino(): #thread function to catch arduino updates from serial
    while(catchSpeeds == true):
        #insert serial catch line and parsing here to update speeds
        #formatting ("m1,m2,m3,m4,arduino_time")
        #Update DR position estimate from info
    return

def absolute2Local(dx_abs,dy_abs,dphi_abs): #takes in absolute reference velocities and decodes to robot frame
    dphi = dphi_abs
    dx = dx_abs*cos(current_location(2))-dy_abs*sin(current_location(2))
    dy = dx_abs*sin(current_location(2))+dy_abs*cos(current_location(2))
    return
