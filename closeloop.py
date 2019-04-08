import hebi
# Virtual spring
lookup = hebi.Lookup()
# change to your name(s)/family(s)
group = lookup.get_group_from_names(["Robot B"], ["J1"])
command = hebi.GroupCommand(group.size)
stiffness = 50.0 # [Nm/rad]

def fbk_handler(feedback):
  command.effort = feedback.position * -stiffness
  group.send_command(command)

group.add_feedback_handler(fbk_handler)
