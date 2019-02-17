#!/usr/bin/env python

import rospy
from system_state.msg import *

def button():
    pub = rospy.Publisher('button_press', ButtonPress, queue_size=1)
    rospy.init_node('button')
    while not rospy.is_shutdown():
        raw_input("Press 'B' to send button press")
        press = ButtonPress("button pressed")
        pub.publish(press)

if __name__ == '__main__':
    try:
        button()
    except rospy.ROSInterruptException:
        pass