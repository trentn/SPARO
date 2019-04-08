import hebi
from math import pi, sin
from time import sleep, time

lookup = hebi.Lookup()

# Wait 2 seconds for the module list to populate
sleep(2.0)

family_name = "arm"
module_name = "J1"

group = lookup.get_group_from_names([family_name], [module_name])
group1 = lookup.get_group_from_names(["arm"], ["J2"])
group2 = lookup.get_group_from_names(["arm"], ["J3"])

if group is None:
  print('Group not found! Check that the family and name of a module on the network')
  print('matches what is given in the source file.')
  exit(1)

group_command  = hebi.GroupCommand(group.size)
group_feedback = hebi.GroupFeedback(group.size)
group_command1  = hebi.GroupCommand(group1.size)
group_feedback1 = hebi.GroupFeedback(group1.size)
group_command2  = hebi.GroupCommand(group2.size)
group_feedback2 = hebi.GroupFeedback(group2.size)

# Start logging in the background
#group.start_log('logs')

freq_hz = 0.5                 # [Hz]
freq    = freq_hz * 2.0 * pi  # [rad / sec]
amp     = pi * 0.25           # [rad] (45 degrees)


sleep(1)
duration = 2.0               # [sec]
start = time()
t = time() - start


while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  group2.get_next_feedback(reuse_fbk=group_feedback)
  #group1.get_next_feedback(reuse_fbk=group_feedback1)

  
  t = time() - start
  group_command2.position = pi/4 #amp* sin((3*freq/2) + t)

  group2.send_command(group_command2)


duration = 2.0               # [sec]
start = time()
t = time() - start

while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  #group.get_next_feedback(reuse_fbk=group_feedback)
  group1.get_next_feedback(reuse_fbk=group_feedback1)
  t = time() - start

  #group_command.position = -amp * sin(freq/2 - t)
  
  #sleep(5)
  group_command1.position = 5*pi/24 #amp* sin((3*freq/2) + t)
  #group_command1.effort = 2.0
 # sleep(1)
  #group.send_command(group_command)
  group1.send_command(group_command1)
  

# Stop logging. `log_file` contains the contents of the file
#log_file = group.stop_log()



duration = 2.0               # [sec]
start = time()
t = time() - start


while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  group.get_next_feedback(reuse_fbk=group_feedback)
  #group1.get_next_feedback(reuse_fbk=group_feedback1)

  
  t = time() - start
  group_command.position = -pi/2 #amp* sin((3*freq/2) + t)

  group.send_command(group_command)
  group1.get_next_feedback(reuse_fbk=group_feedback1)
  group_command1.position = 5*pi/24
  group1.send_command(group_command1)
#  group.send_command(group_command)

#sleep(1)



#sleep(1)
duration = 2.0               # [sec]
start = time()
t = time() - start


while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  group.get_next_feedback(reuse_fbk=group_feedback)
  #group1.get_next_feedback(reuse_fbk=group_feedback1)

  
  t = time() - start
  group_command.position = pi/2 #amp* sin((3*freq/2) + t)

  group.send_command(group_command)
 
  group1.get_next_feedback(reuse_fbk=group_feedback1)
  group_command1.position = 5*pi/24
 # group_command1.effort = 1
  group1.send_command(group_command1)
  #sleep(1)
  #group.send_command(group_command)


duration = 4.0               # [sec]
start = time()
t = time() - start

while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  #group.get_next_feedback(reuse_fbk=group_feedback)
  group1.get_next_feedback(reuse_fbk=group_feedback1)
  t = time() - start

  #group_command.position = -amp * sin(freq/2 - t)
  
  #sleep(5)
  group_command1.position = pi/2 #* sin((freq/2) + t)
 # group_command1.effort = 2.0
 # sleep(1)
  #group.send_command(group_command)
  group1.send_command(group_command1)


#sleep(1)
duration = 4.0               # [sec]
start = time()
t = time() - start


while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  group2.get_next_feedback(reuse_fbk=group_feedback)
  #group1.get_next_feedback(reuse_fbk=group_feedback1)

  
  t = time() - start
  group_command2.position = 0 #amp* sin((3*freq/2) + t)

  group2.send_command(group_command2)
