#!/usr/bin/env python
import math
import time
import json
import rospy
from system_state.msg import *
from system_state.srv import *

from actuation_scripts import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import threading

target_type = {'VALVE1': 0,
                'VALVE2': 1,
                'VALVE3': 2,
                'BREAKER_A': 3,
                'BREAKER_B': 3}

class LED_thread(threading.Thread):
    def __init__(self, mode):
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0

        if mode == 'pre-op':
            self.blink = self.pre_op_blink
        if mode == 'operation':
            self.blink = self.operation
        if mode == 'loading':
            self.blink = self.loading_blink
        if mode == 'move_robot':
            self.blink = self.move_robot
        if mode == 'detect_target':
            self.blink = self.detect_target
        if mode == 'move_endeffector':
            self.blink = self.move_endeffector
        if mode == 'set_target':
            self.blink = self.set_target
        if mode == 'error':
            self.blink = self.error

        self.status_pin = 6
        self.error_pin = 5
        self.locomotion_pin = 17
        self.vision_pin = 27
        self.endeffector_pin = 22
	
        threading.Thread.__init__(self, name="LED %s"%mode)

    def run(self):
        while not self._stopevent.isSet():
            self.blink()

    def pre_op_blink(self):
        GPIO.output(self.status_pin, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(self.status_pin, GPIO.LOW)
        time.sleep(.25)

    def loading_blink(self):
        GPIO.output(self.status_pin, GPIO.HIGH)
        time.sleep(.15)
        GPIO.output(self.status_pin, GPIO.LOW)
        time.sleep(.15)

    def operation(self):
        GPIO.output(self.status_pin, GPIO.HIGH)
        self._stopevent.set()

    def move_robot(self):
        GPIO.output(self.locomotion_pin, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(self.locomotion_pin, GPIO.LOW)
        time.sleep(.0001)
    
    def detect_target(self):
        GPIO.output(self.vision_pin, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(self.vision_pin, GPIO.LOW)
        time.sleep(.0001)

    def move_endeffector(self):
        GPIO.output(self.endeffector_pin, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(self.endeffector_pin, GPIO.LOW)
        time.sleep(.0001)

    def set_target(self):
        GPIO.output(self.endeffector_pin, GPIO.HIGH)
        time.sleep(.50)
        GPIO.output(self.endeffector_pin, GPIO.LOW)
        time.sleep(.25)

    def error(self):
        GPIO.output(self.status_pin, GPIO.LOW)
        GPIO.output(self.error_pin, GPIO.HIGH)
        self._stopevent.set()

    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self,timeout)

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
        self.move_complete = False
        self.state = "PRE-OPERATION"
        self.mission = {}
        self.target = {}
        self.task = 0
        self.num_tasks = 0

        rospy.init_node('System')
        rospy.Subscriber("button_press", ButtonPress, self.handle_button)
        rospy.Subscriber("at_location", AtLocation, self.handle_at_location)
        self.move_commands = rospy.Publisher("move_commands", MoveCommand, queue_size=1)
        self.move_arm = rospy.Publisher("move_arm", MoveArm, queue_size=1)        
        self.turn_endeffector = rospy.Publisher("turn_endeffector", TurnEndEffector, queue_size=1)        
        rospy.loginfo("Initialized system")
        rospy.loginfo("System starting state: %s" % self.state)       


    def handle_button(self, data):
        if self.state == "PRE-OPERATION":
            rospy.loginfo("Received button press '%s'" % data)
            self.button_pressed = True

    def handle_at_location(self, data):
        if self.state == "MOVE_ROBOT":
            if data.at_location == True:
                time.sleep(2)
                self.move_complete = True
            else:
                pass

    def parse_orientation(self, orientation_string):
        if(self.target['types'] == 'VALVE1'):
            return orientation_string[2]
        elif(self.target['types'] == 'VALVE2'):
            return orientation_string[2]
        elif(self.target['types'] == 'VALVE3'):
            return orientation_string[2]

    def parse_current_position(self, orientation_string):
       if(self.target['types'] == 'VALVE3'):
           return orientation_string[3]
       if(self.target['types'] == 'BREAKER_A' or self.target['types'] == 'BREAKER_B'):
           return orientation_string[1:]

    def load_mission(self):
        rospy.wait_for_service('load_mission')
        try:
            get_mission = rospy.ServiceProxy('load_mission', LoadMission)
            self.mission = json.loads(get_mission().json_mission)
            if not self.mission:
                return False
            rospy.loginfo(str(self.mission))
            self.num_tasks = len(self.mission['tasks'])
            return True
        except rospy.ServiceException, e:
            rospy.loginfo("Service call failed: %s" % e)

    def mission_complete(self):
        return self.task >= self.num_tasks

    def set_next_target(self):
        self.target = self.mission['tasks'][self.task]
        self.task += 1

    def move_to_next_target(self):
        self.move_complete = False
        self.move_arm.publish(MoveArm(self.target['arm_reset'][0], self.target['arm_reset'][1], self.target['arm_reset'][2]))
        time.sleep(3)
        self.move_commands.publish(MoveCommand(self.target['station'][0], self.target['station'][1], 0))
        rospy.loginfo("Moving to %f,%f" % (self.target['station'][0],self.target['station'][1]))
        while not self.move_complete:
            pass
        return True

    def detect_target_state_position(self):
        '''
        TODO: update target info with service call return
        '''
        rospy.wait_for_service('detect_target')
        try:
            captured = False
            val = 0.03
            while not captured:
                detect_target = rospy.ServiceProxy('detect_target', DetectTarget)
                target_info = detect_target(target_type[self.target['types']])
                if(target_info.Z != 0):
                    captured = True
                else:
                    val = -val
                    rospy.loginfo("DETECT_TARGET: Moving and trying again...")
                    if(self.target['station_letter'] >= 'A' or self.target['station_letter'] < 'F'):
                        self.target['station'][1] += val
                    else:
                        self.target['station'][0] += val
                    self.move_commands.publish(MoveCommand(self.target['station'][0], self.target['station'][1], 0))

            self.target['position'] = {}
            self.target['position']['X'] = target_info.X
            self.target['position']['Y'] = target_info.Y
            self.target['position']['Z'] = target_info.Z
            self.target['position']['orientation'] = self.parse_orientation(target_info.orientation_state)
            self.target['currentPosition'] = self.parse_current_position(target_info.orientation_state)
            rospy.loginfo('Detected:' + str(target_info))
    
            return True
        except rospy.ServiceException, e:
            rospy.loginfo("Service call failed: %s" % e)
            return False
    
    def target_at_desired(self):
        return False 
    
    def move_end_effector_to_target(self):
        print("in move end effector")
        time.sleep(3)
        try:
            if(self.target['types']=='VALVE1'):
                if(self.target['position']['orientation'] == 'U'):
                    actuate_valve1_up(self.target,self.move_commands,self.move_arm, self.turn_endeffector)
                elif(self.target['position']['orientation'] == 'F'):
                    actuate_valve1_forward(self.target,self.move_commands,self.move_arm, self.turn_endeffector)

            elif(self.target['types'] == 'VALVE2'):
                if(self.target['position']['orientation'] == 'F'):
                    actuate_valve2_forward(self.target,self.move_commands,self.move_arm, self.turn_endeffector)
                    
            elif(self.target['types'] == 'VALVE3'):
                if(self.target['position']['orientation'] == 'U'):
                    actuate_valve3_up(self.target,self.move_commands,self.move_arm, self.turn_endeffector)
                elif(self.target['position']['orientation'] == 'F'):
                    actuate_valve3_forward(self.target,self.move_commands,self.move_arm, self.turn_endeffector)
                
            elif(self.target['types'] == 'BREAKER_A'):
                actuate_breaker_A(self.target,self.move_commands,self.move_arm, self.turn_endeffector)

            elif(self.target['types'] == 'BREAKER_B'):
                actuate_breaker_B(self.target,self.move_commands,self.move_arm, self.turn_endeffector)
                
            return True

        except rospy.ServiceException, e:
            rospy.loginfo("Service call failed: %s" %e)
            return False

    def set_target_to_desired(self):
        #if(self.target['types'] == 'VALVE1'):
        #    self.turn_endeffector.publish(TurnEndEffector(int(self.target['desiredPosition'])))
        #    time.sleep(1)
        return True

    def log_state_change(self, prev_state):
        rospy.loginfo('state change: %s -> %s' %(prev_state, self.state))

    
    def execute(self):
        '''
        PRE-OPERATION state handling
        '''
        if self.state == "PRE-OPERATION":
            led_thread = LED_thread("pre-op") 
            led_thread.start()
            self.task = 0
            # while not self.button_pressed:
            #     pass
            raw_input("Press enter to continue with mission")
            self.state = "LOADING_MISSION"
            self.button_pressed = False
            self.log_state_change("PRE-OPERATION")
            led_thread.join()

        '''
        LOADING_MISSION state handling
        '''
        if self.state == "LOADING_MISSION":
            led_thread = LED_thread("loading")
            led_thread.start()
            if not self.load_mission():
                self.state = "PRE-OPERATION"
            else:
                self.state = "MISSION_STATUS_CHECK"
            self.log_state_change("LOADING_MISSION")
            led_thread.join()

        '''
        MISSION_STATUS_CHECK state handling
        '''
        if self.state == "MISSION_STATUS_CHECK":
            led_thread = LED_thread("operation")
            led_thread.start()
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
            led_thread = LED_thread("move_robot")
            led_thread.start()
            if not self.move_to_next_target():
                self.state = "ERROR"
            else:
                self.state = "DETECT_TARGET"
            self.log_state_change("MOVE_ROBOT")
            led_thread.join()

        '''
        DETECT_TARGET state handling
        '''
        if self.state == "DETECT_TARGET":
            led_thread = LED_thread("detect_target")
            led_thread.start()
            if not self.detect_target_state_position():
                self.state = "ERROR"
            else:
                if self.target_at_desired():
                    self.state = "MISSION_STATUS_CHECK"
                else:
                    self.state = "MOVE_END_EFFECTOR"
            self.log_state_change("DETECT_TARGET")
            led_thread.join()

        '''
        MOVE_END_EFFECTOR state handling
        '''
        if self.state == "MOVE_END_EFFECTOR":
            led_thread = LED_thread("move_endeffector")
            led_thread.start()
            if not self.move_end_effector_to_target():
                self.state = "ERROR"
            else:
                self.state = "SET_TARGET_STATE"
            self.log_state_change("MOVE_END_EFFECTOR")
            led_thread.join()

        '''
        SET_TARGET_STATE state handling
        '''
        if self.state == "SET_TARGET_STATE":
            led_thread = LED_thread("set_target")
            led_thread.start()
            if not self.set_target_to_desired():
                self.state = "ERROR"
            else:
                self.state = "MISSION_STATUS_CHECK"
            
            self.log_state_change("SET_TARGET_STATE")
            led_thread.join()

        '''
        ERROR state handling
        '''
        if self.state == "ERROR":
            led_thread = LED_thread("error")
            led_thread.start()
            rospy.loginfo("SPARO is in an ERROR state!!")
            raw_input("Press ENTER to kill")
            exit()

if __name__ == "__main__":
    status_pin = 6
    error_pin = 5
    locomotion_pin = 17
    vision_pin = 27
    endeffector_pin = 22
    GPIO.setup(status_pin, GPIO.OUT, initial=GPIO.LOW)        
    GPIO.setup(error_pin, GPIO.OUT, initial=GPIO.LOW) 
    GPIO.setup(locomotion_pin, GPIO.OUT, initial=GPIO.LOW) 
    GPIO.setup(vision_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(endeffector_pin, GPIO.OUT, initial=GPIO.LOW) 

    system = System()
    while not rospy.is_shutdown():
        system.execute()
