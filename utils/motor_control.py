#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
	speeds = raw_input("Enter speeds: ")
	speeds = speeds+"\n"
	ser.write(speeds)
