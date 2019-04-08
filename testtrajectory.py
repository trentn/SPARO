import hebi
from math import pi
from time import sleep, time
import numpy as np

lookup = hebi.Lookup()

# Wait 2 seconds for the module list to populate
sleep(2.0)

group = lookup.get_group_from_names(["arm"], ["J1"])
group1 = lookup.get_group_from_names(["arm"],["J2"])

num_joints, num_joints1 = group.size, group1.size
group_feedback = hebi.GroupFeedback(num_joints)
group_feedback1 = hebi.GroupFeedback(num_joints1)


positions = np.zeros((num_joints, 3), dtype=np.float64)
offset = [pi] * num_joints
current_pos = group_feedback.position
positions[:, 0] = current_pos
positions[:, 1] = current_pos + pi/2
positions[:, 2] = current_pos
time_vector = [0, 3, 9]

positions1 = np.zeros((num_joints1, 3), dtype=np.float64)
offset = [pi] * num_joints1
current_pos1 = group_feedback1.position

positions1[:, 0] = current_pos
positions1[:, 1] = current_pos - pi/2
positions1[:, 2] = current_pos

time_vector1 = [0,3,9]
trajectory = hebi.trajectory.create_trajectory(time_vector, positions)
trajectory1 = hebi.trajectory.create_trajectory(time_vector1, positions1)

# Start logging in the background
group.start_log('logs')

group_command = hebi.GroupCommand(num_joints)
duration = trajectory.duration

group_command1 = hebi.GroupCommand(num_joints1)
duration1 = trajectory1.duration
start = time()
t = time() - start

while t < duration:
  # Serves to rate limit the loop without calling sleep
  group.get_next_feedback(reuse_fbk=group_feedback)
  t = time() - start

  pos, vel, acc = trajectory.get_state(t)
  group_command.position = pos
  group_command.velocity = vel
  group.send_command(group_command)


  # Serves to rate limit the loop without calling sleep
  group1.get_next_feedback(reuse_fbk=group_feedback)
#  t1 = time() - start1

  pos1, vel1, acc1 = trajectory1.get_state(t)
  group_command1.position = pos1
  group_command1.velocity = vel1
  group1.send_command(group_command1)


group.stop_log()

