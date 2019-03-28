#!/usr/bin/env python

import rospy
from system_state.msg import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def button():
    pinButton=21
    GPIO.setup(pinButton, GPIO.IN)

    pub = rospy.Publisher('button_press', ButtonPress, queue_size=1)
    rospy.init_node('button')
    while not rospy.is_shutdown():
       # raw_input("Press 'B' to send button press")
        #
        #
        if GPIO.input(21) == GPIO.HIGH:
            press = ButtonPress("button pressed")
            pub.publish(press)

if __name__ == '__main__':
    try:
        button()
    except rospy.ROSInterruptException:
        pass
