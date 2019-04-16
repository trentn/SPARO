#!/usr/bin/env python

from system_state.srv import *
import rospy
import json

locations = {'A':(1.38+.161,0.4),
             'B':(1.075+.161,0.4),
             'C':(0.77+.161,0.4),
             'D':(0.465+.161,0.4),
             'E':(0.33,0.4),
             'F':(0.4,0.33),
             'G':(0.4,0.425+.161),
             'H':(0.4,0.73+.161)}

def arm_rest_position(station_letter):
    if(station_letter >= 'A' and station_letter < 'F'):
        return (.809, -90, 45)
    else:
        return (.809, -90, -45)

def handle_load_mission(req):
	#opening the mission file 
    mission = {}

    try:
        myfile=open("/media/usb/mission.txt")
        content = myfile.read()
        eachline=content.splitlines()
        mission["tasks"] = []
        for j in range(len(eachline)-1):
            r1=locations[eachline[j][0]]
            r4=arm_rest_position(eachline[j][0])
            if eachline[j][1]=="V" and eachline[j][2]=="1":
                r2='VALVE1'
                r3=eachline[j][4:]
            if eachline[j][1]=="V" and eachline[j][2]=="2":
                r2='VALVE2'
                r3=eachline[0][4:]
            if eachline[j][1]=="V" and eachline[j][2]=="3":
                r2='VALVE3'
                if eachline[j][4]==0:
                    r3='Open'
                if eachline[j][4]==1:
                    r3='closed'
            if eachline[j][1]=="A":
                r2='BREAKER'
                if eachline[j][6]=="U":
                    r31='Up'
                else:
                    r31='Down'
                if eachline[j][11]=="U":
                    r32='Up'
                else:
                    r32='Down'
                if eachline[j][16]=="U":
                    r33='Up'
                else:
                    r33='Down'    
            if eachline[j][1]=="B":
                r2='BREAKER' 
                if eachline[j][6]=="U":
                    r31='Up'
                else:
                    r31='Down'
                if eachline[j][11]=="U":
                    r32='Up'
                else:
                    r32='Down'
                if eachline[j][16]=="U":
                    r33='Up'
                else:
                    r33='Down'

            if len(eachline[j])==17:
                result={"station":r1, "types":r2, "desiredPosition":[r31,r32,r33], "arm_reset":r4}
            else:
                result={"station":r1, "types":r2, "desiredPosition":r3,"arm_reset":r4}
            mission["tasks"].append(result)

        mission["time"] = int(eachline[j+1])
        rospy.loginfo("Mission Loaded: %s" % str(mission))

    except:
        rospy.loginfo("Mission failed to load")
    
    finally:
        return LoadMissionResponse(json.dumps(mission))

def mission_loader():
    rospy.init_node("mission_loader")
    s = rospy.Service("load_mission", LoadMission, handle_load_mission)
    rospy.loginfo("Ready to load missions")
    rospy.spin()

if __name__ == "__main__":
    mission_loader()
