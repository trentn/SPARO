#!/usr/bin/env python

from system_state.srv import *
import rospy
import json

mission = {}

def handle_load_mission(req):
    s = raw_input("Load mission? [y/n]")
    if s[0] == 'y':
        mission['mission'] = 'loaded'
    	rospy.loginfo("Loaded Mission")
    else:
	rospy.loginfo("Mission failed to load")
    return LoadMissionResponse(json.dumps(mission))

def mission_loader():
    rospy.init_node("mission_loader")
    s = rospy.Service("load_mission", LoadMission, handle_load_mission)
    rospy.loginfo("Ready to load missions")
    rospy.spin()

if __name__ == "__main__":
    mission_loader()
