#!/usr/bin/env python

from system_state.srv import *
import rospy
import json

locations = {'A':(1.30+.161,0.33),
             'B':(1.03+.161,0.33),
             'C':(0.70+.161,0.33),
             'D':(0.425+.161,0.33),
             'E':(0.28,0.33),
             'F':(0.33,0.30),
             'G':(0.33,0.425+.161),
             'H':(0.33,0.70+.161)}

def arm_rest_position(station_letter):
    if(station_letter >= 'A' and station_letter < 'F'):
        return (.809, -90, 45)
    else:
        return (.809, -90, -45)

def handle_load_mission(req):
	#opening the mission file 
    mission = {}

    try:
        myfile=open("./mission.txt")
        content = myfile.read()
        eachline=content.splitlines()
        mission["tasks"] = []
        for j in range(len(eachline)-1):
            r1=eachline[j][0]
            location = locations[r1]
            r4=arm_rest_position(eachline[j][0])
            if eachline[j][1]=="V" and eachline[j][2]=="1":
                r2='VALVE1'
                r3=-int(eachline[j][4:])
            if eachline[j][1]=="V" and eachline[j][2]=="2":
                r2='VALVE2'
                r3=-int(eachline[j][4:])
            if eachline[j][1]=="V" and eachline[j][2]=="3":
                r2='VALVE3'
                if eachline[j][4]=='0':
                    r3='O'
                if eachline[j][4]=='1':
                    r3='C'
            if eachline[j][1] == 'A' or eachline[j][1] == 'B':
                r2='BREAKER_%c'%eachline[j][1]
                breaker_states = list(filter(None, eachline[j][3:].split('B')))
                r3 = ['-','-','-']
                for state in breaker_states:
                    r3[int(state[0])-1] = '0' if state[2] == 'D' else '1'

            result={"station_letter":r1, "station":location, "types":r2, "desiredPosition":r3,"arm_reset":r4}
            mission["tasks"].append(result)

        mission["time"] = int(eachline[j+1])
        rospy.loginfo("Mission Loaded: %s" % str(mission))
    
    
    except Exception:
        rospy.loginfo("Mission failed to load")
        raise Exception
        
    finally:
        return LoadMissionResponse(json.dumps(mission))
        
def mission_loader():
    rospy.init_node("mission_loader")
    s = rospy.Service("load_mission", LoadMission, handle_load_mission)
    rospy.loginfo("Ready to load missions")
    rospy.spin()

if __name__ == "__main__":
    mission_loader()
