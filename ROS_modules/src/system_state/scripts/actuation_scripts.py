import math
import time
import rospy
from system_state.msg import *

def actuate_valve1_up(target, move_commands, move_arm, turn_endeffector):
    print("entered small gate valve up protocol")
    h_needed = .4635 - target['position']['Y'] + .01
    print(h_needed)
    d_needed = math.sqrt(.455**2-(h_needed-.205+.155)**2) - 0.02 + .07  #.01 is a buffer
    print(d_needed)
    print(d_needed - target['position']['Z'])
    print(target['station'][1])


    if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):
        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.035 ,
                                        target['station'][1] + (d_needed - target['position']['Z']),
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
        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.035 ,
                                           target['station'][1] + (d_needed - target['position']['Z']),
                                            0))
        
        time.sleep(3)
        move_arm.publish(MoveArm(h_needed-.03,
                                90,
                                target['arm_reset'][2]))                
        time.sleep(2)

        turn_endeffector.publish(TurnEndEffector(int(target['desiredPosition'])))

        time.sleep(2)

        move_arm.publish(MoveArm(h_needed + .01,
                                90,
                                target['arm_reset'][2]))

        time.sleep(1)              

    else:
        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])  ,
                                        target['station'][1] + target['position']['X' ] - 0.025,
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
        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])  ,
                                        target['station'][1] + target['position']['X' ] - 0.025,
                                            0))
        
        time.sleep(3)
        move_arm.publish(MoveArm(h_needed-.03,
                                90,
                                target['arm_reset'][2]))                
        time.sleep(2)

        turn_endeffector.publish(TurnEndEffector(int(target['desiredPosition'])))

        time.sleep(2)

        move_arm.publish(MoveArm(h_needed + .01,
                                90,
                                target['arm_reset'][2]))

        time.sleep(1)

def actuate_valve1_forward(target, move_commands, move_arm, turn_endeffector):

    print("entered forward small gate valve protocol")
    
    h_needed = .4635 - target['position']['Y'] #h needed from ground
    print(h_needed)
    d_needed = math.sqrt(.455**2-(h_needed-.205-.07)**2) + .15 #.07 is short end effector / .15 long end effector / .205 dist from arm to ground
    print(d_needed)
    print(d_needed - target['position']['Z'])
    print(target['station'][1])

    if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):

        #line up step

        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.015 + .03,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .05, #no back off distance
                                            0))
        time.sleep(4)
        print("First arm movement")
        move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
        time.sleep(2)
        
        #drive into it 
        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.015 +.03,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.09, #-.02 engage distance
                                            0))
        time.sleep(5)

        turn_endeffector.publish(TurnEndEffector(int(target['desiredPosition'])))
        
        time.sleep(2)
        #back up
        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.015 + .03,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .02, #no back off distance
                                            0))           
        time.sleep(5)
    else:

        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - 0.03, #no back off distance
                                            0))
        time.sleep(4)
        print("First arm movement")
        move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
        time.sleep(5)
        
        #drive into it 
        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) - .07,
                                        target['station'][1] + target['position']['X' ] - .03, #no back off distance
                                            0))
        time.sleep(5)

        turn_endeffector.publish(TurnEndEffector(int(target['desiredPosition'])))

        time.sleep(4)
        #back up
        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) + .02,
                                        target['station'][1] + target['position']['X' ] - 0.3, #no back off distance
                                        0))
        time.sleep(5)

def actuate_valve2_forward(target, move_commands, move_arm, turn_endeffector):

    print("entered large gate valve protocol")

    h_needed = .4635 - target['position']['Y'] #h needed from ground
    print(h_needed)
    d_needed = math.sqrt(.455**2-(h_needed-.205-.065)**2) + .15 #.07 is short end effector / .15 long end effector / .205 dist from arm to ground
    print(d_needed)
    print(d_needed - target['position']['Z'])
    print(target['station'][1])



    if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):

        #line up step

        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (d_needed - target['position']['Z'] + .08), #no back off distance
                                            0))
        time.sleep(4)
        print("First arm movement")
        move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
        time.sleep(5)
        
        #drive into it 
        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #.02 engage distance
                                            0))
        time.sleep(5)
        print(target['desiredPosition'])
        turn_endeffector.publish(TurnEndEffector(int(target['desiredPosition'])))

        time.sleep(3)
        #back up
        move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .03, #.05 back off distance
                                            0))           
        time.sleep(5)
    else:

        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - 0.03, #no back off distance
                                            0))
        time.sleep(4)
        print("First arm movement")
        move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
        time.sleep(5)
        
        #drive into it 
        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) - .02,
                                        target['station'][1] + target['position']['X' ] - 0.03, #no back off distance
                                            0))
        time.sleep(5)
        
        turn_endeffector.publish(TurnEndEffector(int(target['desiredPosition'])))

        time.sleep(3)

        move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - 0.03, #no back off distance
                                            0))
        time.sleep(5)

def actuate_valve3_forward(target, move_commands, move_arm, turn_endeffector):

    print("entered forward shuttlecock protocol")

    rotation_command = 0

    if target['desiredPosition'] == target['currentPosition']:
        print('Already at position')
        return
    elif(target['desiredPosition'] == 'O'):
        h_needed = .4635 - target['position']['Y'] #h needed from ground
        print(h_needed)
        d_needed = math.sqrt(.455**2-(h_needed-.205-.065)**2) + .15 #.07 is short end effector / .15 long end effector / .205 dist from arm to ground
        print(d_needed)
        print(d_needed - target['position']['Z'])
        print(target['station'][1])
        rotation_command = 120
        if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):  #TODO
        #line up step

            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.02,
                                        target['station'][1] + (d_needed - target['position']['Z'] + .1), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(5)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.02,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #.02 engage distance
                                            0))
            time.sleep(5)

            turn_endeffector.publish(TurnEndEffector(rotation_command))

            time.sleep(3)

            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.02,
                                        target['station'][1] + (d_needed - target['position']['Z']), #.05 back off distance
                                            0))           
            time.sleep(5)

        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) + .1, #no back off distance
                                        target['station'][1] + target['position']['X' ] - 0.03 -.06, 
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(5)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) - .06, #no back off distance
                                        target['station'][1] + target['position']['X' ] - 0.03 - .06, 
                                            0))
            time.sleep(5)

            turn_endeffector.publish(TurnEndEffector(rotation_command))

            time.sleep(3)
        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']), #no back off distance
                                        target['station'][1] + target['position']['X' ] - 0.03 -.06, 
                                        0))
            time.sleep(3)

    elif(target['desiredPosition'] == 'C'):
        h_needed = .4635 - target['position']['Y'] - .05 #h needed from ground
        print(h_needed)
        d_needed = math.sqrt(.455**2-(h_needed-.205-.065)**2) + .15 #.07 is short end effector / .15 long end effector / .205 dist from arm to ground
        print(d_needed)
        print(d_needed - target['position']['Z'])
        print(target['station'][1])
        rotation_command = -120
        if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):
        #line up step

            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(5)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.06, #.02 engage distance
                                            0))
            time.sleep(5)

            print rotation_command

            turn_endeffector.publish(TurnEndEffector(int(rotation_command)))

            time.sleep(3)

            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .03, #.05 back off distance
                                            0))           
            time.sleep(5)

        else: #TODO
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']), #no back off distance
                                        target['station'][1] + target['position']['X' ] - 0.03, 
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(5)
        
            #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) - .07, #no back off distance
                                        target['station'][1] + target['position']['X' ] - 0.03, 
                                            0))
            time.sleep(5)

            print rotation_command

            turn_endeffector.publish(TurnEndEffector(rotation_command))

            time.sleep(3)
            #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']), #no back off distance
                                        target['station'][1] + target['position']['X' ] - 0.03, 
                                        0))
            time.sleep(5)
    
def actuate_valve3_up(target, move_commands, move_arm, turn_endeffector):

    print("entered up shuttlecock protocol")

    rotation_command = 0

    if target['desiredPosition'] == target['currentPosition']:
        print('Already at position')
        return
    elif(target['desiredPosition'] == 'O'):

        h_needed = .4635 - target['position']['Y'] + .01
        print(h_needed)
        d_needed = math.sqrt(.455**2-(h_needed-.205+.155)**2) + .07
        print(d_needed)
        print(d_needed - target['position']['Z'])
        print(target['station'][1])

        rotation_command = -110

        if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.12,
                                        .34,
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed - .05,
                                 90,
                                target['arm_reset'][2]))
            time.sleep(3)

            
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X'] - .02,
                                        .34,
                                        0))
            
            time.sleep(3)
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] - .02,
                                           .3,
                                          0))
            time.sleep(3)
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + -.02,
                                           .5,
                                          0))

            time.sleep(2)
            move_arm.publish(MoveArm(h_needed + .05,
                                0,
                                target['arm_reset'][2]))

        else: #TODO
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])  ,
                                        target['station'][1] + target['position']['X' ] - 0.025,
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
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])  ,
                                        target['station'][1] + target['position']['X' ] - 0.025,
                                            0))
        
            time.sleep(3)
            move_arm.publish(MoveArm(h_needed-.03,
                                90,
                                target['arm_reset'][2]))                
            time.sleep(2)

            turn_endeffector.publish(TurnEndEffector(rotation_command))

            time.sleep(2)

            move_arm.publish(MoveArm(h_needed + .01,
                                90,
                                target['arm_reset'][2]))

            time.sleep(1)

    elif(target['desiredPosition'] == 'C'):
        h_needed = .4635 - target['position']['Y']
        print(h_needed)
        d_needed = math.sqrt(.455**2-(h_needed-.205+.155)**2) + .07
        print(d_needed)
        print(d_needed - target['position']['Z'])
        print(target['station'][1])
        
        rotation_command = 110

        if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                        .33,
                                            0))
            time.sleep(4)
            move_arm.publish(MoveArm(.52,
                                 45,
                                target['arm_reset'][2]))
            time.sleep(5)

            move_arm.publish(MoveArm(.47,
                                 45,
                                target['arm_reset'][2]))
            time.sleep(2)
            move_arm.publish(MoveArm(.43,
                                70,
                                target['arm_reset'][2]))
            time.sleep(3)
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + 0.03,
                                           .38,
                                            0))
            time.sleep(1)
            move_arm.publish(MoveArm(.43,
                                60,
                                60))

            time.sleep(3)

            move_arm.publish(MoveArm(target['arm_reset'][0],
                                        target['arm_reset'][1],
                                        target['arm_reset'][2]))
            
            time.sleep(2)
         

        else: #TODO
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])  ,
                                        target['station'][1] + target['position']['X' ] - 0.035,
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
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])  ,
                                        target['station'][1] + target['position']['X' ] - 0.035,
                                            0))
        
            time.sleep(3)
            move_arm.publish(MoveArm(h_needed-.03,
                                90,
                                target['arm_reset'][2]))                
            time.sleep(2)

            turn_endeffector.publish(TurnEndEffector(rotation_command))

            time.sleep(2)

            move_arm.publish(MoveArm(h_needed + .01,
                                90,
                                target['arm_reset'][2]))

            time.sleep(1)
    
def actuate_breaker_A(target, move_commands, move_arm, turn_endeffector):

    print("entered breaker A protocol")

    h_needed = .4635 - target['position']['Y'] #h needed from ground
    print(h_needed)
    d_needed = math.sqrt(.455**2-(h_needed-.205-.07)**2) + .15 #.07 is short end effector / .15 long end effector / .205 dist from arm to ground
    print(d_needed)
    print(d_needed - target['position']['Z'])
    print(target['station'][1])

    if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):
        
        
        #TODO: if statements 

        if(target['currentPosition'][0] == target['desiredPosition'][0]):
            print('First breaker in correct position')    
        elif(target['currentPosition'][0] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .09,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .05, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ]  +.09,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.09,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .02, #no back off distance
                                            0))           
            time.sleep(5)
            
        else:
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .09,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .09,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.06, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.09,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][1] == target['desiredPosition'][1]):
            print('Second breaker in correct position')
        elif(target['currentPosition'][1] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .05,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ]+.05,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .02, #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][2] == target['desiredPosition'][2]):
            print('Third breaker in correct position')
        elif(target['currentPosition'][2] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] - .01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] - .01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)
    
    else:

        if(target['currentPosition'][0] == target['desiredPosition'][0]):
            print('First breaker in correct position')    
        elif(target['currentPosition'][0] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) + .05,
                                        target['station'][1]  + target['position']['X' ] - .09, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1] + target['position']['X' ]  -.09, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0]+ (d_needed - target['position']['Z']) + .02,
                                        target['station'][1] + target['position']['X' ] -.09 , #no back off distance
                                            0))           
            time.sleep(5)
            
        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - .09, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.06,
                                        target['station'][1] + target['position']['X' ] - .09 , #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] -.09, #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][1] == target['desiredPosition'][1]):
            print('Second breaker in correct position')
        elif(target['currentPosition'][1] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - .05, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0]  + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1]+ target['position']['X' ] -.05, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) + .02,
                                        target['station'][1] + target['position']['X' ]-.05, #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] -.05, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1] + target['position']['X' ] -.05, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] -.05, #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][2] == target['desiredPosition'][2]):
            print('Third breaker in correct position')
        elif(target['currentPosition'][2] == '1'):
            move_commands.publish(MoveCommand(target['station'][0]  + (d_needed - target['position']['Z']),
                                        target['station'][1]+ target['position']['X' ] + .01, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1] + target['position']['X' ] +.01, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] +.01, #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] +.01, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0]+ (d_needed - target['position']['Z'])-.07,
                                        target['station'][1]  + target['position']['X' ] +.01, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0]+ (d_needed - target['position']['Z']),
                                        target['station'][1]  + target['position']['X' ] + .01, #no back off distance
                                            0))           
            time.sleep(5)

def actuate_breaker_B(target, move_commands, move_arm, turn_endeffector):

    print("entered breaker B protocol")

    h_needed = .4635 - target['position']['Y'] #h needed from ground
    print(h_needed)
    d_needed = math.sqrt(.455**2-(h_needed-.205-.07)**2) + .15 #.07 is short end effector / .15 long end effector / .205 dist from arm to ground
    print(d_needed)
    print(d_needed - target['position']['Z'])
    print(target['station'][1])

    if(target['station_letter'] >= 'A' and target['station_letter'] < 'F'):
        
        if(target['currentPosition'][0] == target['desiredPosition'][0]):
            print('First breaker in correct position')    
        elif(target['currentPosition'][0] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .09,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .05, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ]  +.09,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.09,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .02, #no back off distance
                                            0))           
            time.sleep(5)
            
        else:
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .09,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .09,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.06, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.09,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][1] == target['desiredPosition'][1]):
            print('Second breaker in correct position')
        elif(target['currentPosition'][1] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] + .05,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ]+.05,
                                        target['station'][1] + (d_needed - target['position']['Z']) + .02, #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] +.05,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][2] == target['desiredPosition'][2]):
            print('Third breaker in correct position')
        elif(target['currentPosition'][2] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] - .01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] -.01,
                                        target['station'][1] + (d_needed - target['position']['Z'])-.07, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] - target['position']['X' ] - .01,
                                        target['station'][1] + (d_needed - target['position']['Z']), #no back off distance
                                            0))           
            time.sleep(5)
    
    else:

        if(target['currentPosition'][0] == target['desiredPosition'][0]):
            print('First breaker in correct position')    
        elif(target['currentPosition'][0] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) + .05,
                                        target['station'][1]  + target['position']['X' ] - .09, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1] + target['position']['X' ]  -.09, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0]+ (d_needed - target['position']['Z']) + .02,
                                        target['station'][1] + target['position']['X' ] -.09 , #no back off distance
                                            0))           
            time.sleep(5)
            
        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - .09, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.06,
                                        target['station'][1] + target['position']['X' ] - .09 , #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] -.09, #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][1] == target['desiredPosition'][1]):
            print('Second breaker in correct position')
        elif(target['currentPosition'][1] == '1'):
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] - .05, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0]  + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1]+ target['position']['X' ] -.05, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']) + .02,
                                        target['station'][1] + target['position']['X' ]-.05, #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] -.05, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1] + target['position']['X' ] -.05, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] -.05, #no back off distance
                                            0))           
            time.sleep(5)



        if(target['currentPosition'][2] == target['desiredPosition'][2]):
            print('Third breaker in correct position')
        elif(target['currentPosition'][2] == '1'):
            move_commands.publish(MoveCommand(target['station'][0]  + (d_needed - target['position']['Z']),
                                        target['station'][1]+ target['position']['X' ] + .01, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z'])-.07,
                                        target['station'][1] + target['position']['X' ] +.01, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] +.01, #no back off distance
                                            0))           
            time.sleep(5)
        else:
            move_commands.publish(MoveCommand(target['station'][0] + (d_needed - target['position']['Z']),
                                        target['station'][1] + target['position']['X' ] +.01, #no back off distance
                                            0))
            time.sleep(4)
            print("First arm movement")
            move_arm.publish(MoveArm(h_needed,
                                 0,
                                target['arm_reset'][2]))
            time.sleep(2)
        
        #drive into it 
            move_commands.publish(MoveCommand(target['station'][0]+ (d_needed - target['position']['Z'])-.07,
                                        target['station'][1]  + target['position']['X' ] +.01, #-.02 engage distance
                                            0))
            time.sleep(5)

        #back up
            move_commands.publish(MoveCommand(target['station'][0]+ (d_needed - target['position']['Z']),
                                        target['station'][1]  + target['position']['X' ] + .01, #no back off distance
                                            0))           
            time.sleep(5)