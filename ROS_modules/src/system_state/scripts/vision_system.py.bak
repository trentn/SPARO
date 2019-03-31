#!/usr/bin/env python

from system_state.srv import *
import rospy
import json

def handle_detect_target(req):
    return DetectTargetResponse(json.dumps({'type':'valve', 'orientation':'up'}),0,0,0)

def vision_node():
    rospy.init_node("vision_system")
    s = rospy.Service("detect_target", DetectTarget, handle_detect_target)
    rospy.spin()

if __name__ == "__main__":
    vision_node()