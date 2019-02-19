#!/usr/bin/env python

from system_state.srv import *
import rospy

def handle_move_robot(req):
    raw_input("Press ENTER to send move complete")
    rospy.loginfo("X:%d Y:%d" %(req.X, req.Y))
    return MoveRobotResponse(True)

def locomotion_node():
    rospy.init_node("locomotion")
    rospy.loginfo("Locomotion system is running")
    s = rospy.Service("move_robot", MoveRobot, handle_move_robot)
    rospy.spin()

if __name__ == "__main__":
    locomotion_node()
