#!/usr/bin/env python

from system_state.srv import *
import rospy
import json

def handle_move_endeffector(req):
    raw_input("Press ENTER to send move complete")
    rospy.loginfo("X:%d Y:%d Z:%d" %(req.X, req.Y, req.Z))
    return MoveEndEffectorResponse(True)

def handle_set_target(req):
    raw_input("Press ENTER to send set target complete")
    rospy.loginfo("desired state: %s" % json.dumps(req.json_desiredstate))
    return SetTargetStateResponse(True)

def endeffector_node():
    rospy.init_node("endeffector")
    rospy.loginfo("End Effector system is running")
    s = rospy.Service("move_endeffector", MoveEndEffector, handle_move_endeffector)
    s1 = rospy.Service("set_target", SetTargetState, handle_set_target)
    rospy.spin()

if __name__ == "__main__":
    endeffector_node()
