import numpy as np
import math
import time
#import rospy
import hebi
import threading


arm_log = open("arm_log.log",'w',buffering=1)
at_angle = False

lookup = hebi.Lookup()

time.sleep(2.0)
print("Arm node Started")

#pub = rospy.Publisher("at_angle", AtAngle, queue_size=1)

for entry in lookup.entrylist:
    print(entry)
family_name = "arm"

group = lookup.get_group_from_names([family_name],["J1","J2","J3"]) #Make names more intuitive

if group is None:
    print("Group not found! Check that the family and module name are on the network matches what is given in the source file.")
    exit(1)

command = hebi.GroupCommand(group.size)
feedback = hebi.GroupFeedback(group.size)

desired_angles = np.empty(group.size,dtype=np.float64)
desired_angles[0] = 90.0/180.*math.pi
desired_angles[1] = 90./180.*math.pi
desired_angles[2] = 0.0

HEBI_talk = True

command.position_limit_max = [80./180.*math.pi,90./180.*math.pi,90./180.*math.pi]
command.position_limit_min = [-180./180.*math.pi,0,-90./180.*math.pi]

period = .01

start = time.time()
t = time.time()-start


def command_HEBIs():
    global desired_angles
    print("entered hebi loop")
    while HEBI_talk:
        command.position = desired_angles
        group.send_command(command)

        time.sleep(period)
        t = time.time()-start
    print("exited hebi loop")
    return

HEBI_thread = threading.Thread(target=command_HEBIs,args=())
HEBI_thread.start()

while True:
    position_string = input("Enter desired position: ")
    positions = position_string.split(',')
    z = float(positions[0])
    end_angle = float(positions[1])/180.0*math.pi


    print((z-.2032-.0635*math.cos(end_angle)+.1435*math.sin(end_angle))/.46355)
    desired_angles[1] = .1+math.asin((z-.2032-.0635*math.cos(end_angle)+.1435*math.sin(end_angle))/.46355)
    desired_angles[0] = float(-end_angle-desired_angles[1]+0.1)
    desired_angles[2] = float(positions[2])/180.0*math.pi

    print(desired_angles[0]*180/math.pi)
    print(desired_angles[1])
    
    if(desired_angles[0] == -999./180*math.pi):
        break

HEBI_talk = False
HEBI_thread.join()
