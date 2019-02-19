#!/usr/bin/env python

from system_state.srv import *
import rospy

def handle_move_endeffector(req):
    raw_input("Press ENTER to send move complete")
    rospy.loginfo("X:%d Y:%d Z:%d" %(req.X, req.Y, req.Z))
    return MoveEndEffectorResponse(True)

def endeffector_node():
    rospy.init_node("endeffector")
    rospy.loginfo("End Effector system is running")
    s = rospy.Service("move_endeffector", MoveEndEffector, handle_move_endeffector)
    rospy.spin()

if __name__ == "__main__":
    endeffector_node()
