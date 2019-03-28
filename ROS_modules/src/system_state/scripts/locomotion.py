#!/usr/bin/env python

from system_state.srv import *
import rospy

def handle_move_robot(req):
    s = raw_input("Move complete? [y/n]")
    rospy.loginfo("X:%d Y:%d" %(req.X, req.Y))
    if s[0] == 'y':
        return MoveRobotResponse(True)
    else:
        return MoveRobotResponse(False)

def locomotion_node():
    rospy.init_node("locomotion")
    rospy.loginfo("Locomotion system is running")
    s = rospy.Service("move_robot", MoveRobot, handle_move_robot)
    rospy.spin()

if __name__ == "__main__":
    locomotion_node()
