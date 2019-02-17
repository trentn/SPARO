#!/usr/bin/env python

from system_state.srv import *
import rospy

def handle_move_endeffector(req):
    rospy.loginfo("X:%d Y:%d Z:%d" %(req.X, req.Y, req.Z))
    return MoveEndEffectorResponse(True)

def vision_node():
    rospy.init_node("endeffector")
    s = rospy.Service("move_endeffector", MoveEndEffector, handle_move_endeffector)
    rospy.spin()

if __name__ == "__main__":
    vision_node()