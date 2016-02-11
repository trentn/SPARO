import math
import time
import rospy
from system_state.msg import *

def actuate_valve1_up(target, move_commands, move_arm):
    print("entered arm control valve 1")
    h_needed = .4635 + target['position']['Y'] + .01
    print(h_needed)
    y_needed = math.sqrt(.455**2-(h_needed-.205+.155)**2) - 0.02 + .07
    print(y_needed)
    print(y_needed - target['position']['Z'])
    print(target['station'][1])
    raw_input()
    move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (y_needed - target['position']['Z']),
                                            0))
    
    time.sleep(4)
    print("First arm movement")
    move_arm.publish(MoveArm(.52,
                                    90,
                                    target['arm_reset'][2]))

    time.sleep(5)
    print("Second arm movement")
    move_arm.publish(MoveArm(h_needed,
                                    90,
                                    target['arm_reset'][2]))

    time.sleep(3)
    move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                           target['station'][1] + (y_needed - target['position']['Z']),
                                            0))
    time.sleep(3)
    move_arm.publish(MoveArm(h_needed-.02,
                                    90,
                                    target['arm_reset'][2]))
                    
    time.sleep(5)


def actuate_valve1_up_short(target, move_commands, move_arm):
    print("entered arm control valve 1")
    h_needed = .4635 + target['position']['Y'] + .01
    print(h_needed)
    y_needed = math.sqrt(.455**2-(h_needed-.205+.155)**2) - 0.02 + .07
    print(y_needed)
    print(y_needed - target['position']['Z'])
    print(target['station'][1])
    raw_input()
    move_commands.publish(MoveCommand(target['station'][1] + (y_needed - target['position']['Z']),
                                      target['station'][0] - target['position']['X' ] + 0.03,
                                      0))
    
    time.sleep(4)
    print("First arm movement")
    move_arm.publish(MoveArm(.52,
                                    90,
                                    target['arm_reset'][2]))

    time.sleep(5)
    print("Second arm movement")
    move_arm.publish(MoveArm(h_needed,
                                    90,
                                    target['arm_reset'][2]))

    time.sleep(3)
    move_commands.publish(MoveCommand(target['station'][1] + (y_needed - target['position']['Z']),
                                      target['station'][0] - target['position']['X' ] + 0.03,
                                      0))
    time.sleep(3)
    move_arm.publish(MoveArm(h_needed-.02,
                                    90,
                                    target['arm_reset'][2]))
                    
    time.sleep(5)
