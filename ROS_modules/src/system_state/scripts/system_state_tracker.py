#!/usr/bin/env python

import json
import rospy
from system_state.msg import *
from system_state.srv import *


class System:
    def __init__(self):
        '''
        self.states = ["PRE-OPERATION", 
                       "LOADING_MISSION",
                       "MISSION_STATUS_CHECK",
                       "MOVE_ROBOT",
                       "DETECT_TARGET",
                       "MOVE_END_EFFECTOR",
                       "SET_TARGET_STATE"]
        '''
        self.button_pressed = False
        self.state = "PRE-OPERATION"
        self.mission = {}
        self.target = {}


        rospy.init_node('System')
        rospy.Subscriber("button_press", ButtonPress, self.handle_button)
        rospy.loginfo("Initialized system")
        rospy.loginfo("System starting state: %s" % self.state)
        
        

    def handle_button(self, data):
        rospy.loginfo("Received button press '%s'" % data)
        if self.state == "PRE-OPERATION":
            self.button_pressed = True

    def load_mission(self):
        rospy.wait_for_service('load_mission')
        try:
            get_mission = rospy.ServiceProxy('load_mission', LoadMission)
            self.mission = json.loads(get_mission().json_mission)
            return True
        except rospy.ServiceException, e:
            rospy.loginfo("Service call failed: %s" % e)

    def mission_complete(self):
        rospy.loginfo(str(self.mission))
        return True

    def set_next_target(self):
        target = {}

    def move_to_next_target(self):
        return True

    def detect_target_state_position(self):
        return True
    
    def target_at_desired(self):
        return False
    
    def set_target_to_desired(self):
        return True

    def move_end_effector_to_target(self):
        return True

    def log_state_change(self, prev_state):
        rospy.loginfo('state change: %s -> %s' %(prev_state, self.state))

    def execute(self):
        '''
        PRE-OPERATION state handling
        '''
        if self.state == "PRE-OPERATION":
            while not self.button_pressed:
                pass
            self.state = "LOADING_MISSION"
            self.button_pressed = False
            self.log_state_change("PRE-OPERATION")

        '''
        LOADING_MISSION state handling
        '''
        if self.state == "LOADING_MISSION":
            if not self.load_mission():
                self.state = "PRE-OPERATION"
            else:
                self.state = "MISSION_STATUS_CHECK"
            self.log_state_change("LOADING_MISSION")

        '''
        MISSION_STATUS_CHECK state handling
        '''
        if self.state == "MISSION_STATUS_CHECK":
            if self.mission_complete():
                self.state = "PRE-OPERATION"
            else:
                self.set_next_target()
                self.state = "MOVE_ROBOT"
            self.log_state_change("MISSION_STATUS_CHECK")

        '''
        MOVE_ROBOT state handling
        '''
        if self.state == "MOVE_ROBOT":
            if not self.move_to_next_target():
                self.state = "ERROR"
            else:
                self.state = "DETECT_TARGET"
            
            self.log_state_change("MOVE_ROBOT")

        '''
        DETECT_TARGET state handling
        '''
        if self.state == "DETECT_TARGET":
            if not self.detect_target_state_position():
                self.state = "ERROR"
            else:
                if self.target_at_desired():
                    self.state = "MISSION_STATUS_CHECK"
                else:
                    self.state = "MOVE_END_EFFECTOR"

            self.log_state_change("DETECT_TARGET")
        
        '''
        MOVE_END_EFFECTOR state handling
        '''
        if self.state == "MOVE_END_EFFECTOR":
            if not self.move_end_effector_to_target():
                self.state = "ERROR"
            else:
                self.state = "SET_TARGET_STATE"
            self.log_state_change("MOVE_END_EFFECTOR")

        '''
        SET_TARGET_STATE state handling
        '''
        if self.state == "SET_TARGET_STATE":
            if not self.set_target_to_desired():
                self.state = "ERROR"
            else:
                self.state = "MISSION_STATUS_CHECK"
            
            self.log_state_change("SET_TARGET_STATE")

        '''
        ERROR state handling
        '''
        if self.state == "ERROR":
            rospy.loginfo("SPARO is in an ERROR state!!")
            raw_input("Press ENTER to kill")
            exit()

if __name__ == "__main__":
    system = System()
    while not rospy.is_shutdown():
        system.execute()