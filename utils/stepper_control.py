#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
	angle = raw_input("Enter angle: ")
	angle = angle+"\n"
	ser.write(angle)
