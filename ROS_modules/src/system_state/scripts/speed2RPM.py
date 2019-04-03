import numpy as np
import math
#####################################################################
# motor layout                 +1-                                  #
#                         -           +                             #
# <x+                     2           4                             #
# vy+                     +           -                             #
# phi ccw+                     -3+                                  #
#####################################################################

#Note that absolute x and y movement is tied inherently with the phi position.
#This function takes commands in the robots frame of reference

## TODO: change this to use a kinematics matrix

def  speed2RPM(dx,dy,dphi):
    wheel_d = .1524 #wheel diameter in meters (6")
    wheel_dist_per_rev = wheel_d*math.pi
    outer_d = .4570 #diameter of outer robot in meters (2')

    min_rpm = 0 #to be updated if I find if there is an actuation minimum
    max_rpm = 50 #to be determined experimentally. Spec sheet 80rpm
    max_rps = max_rpm/60 #slightly more useful in calculations
    phi_rads_per_rev = wheel_dist_per_rev/(outer_d/2) #phi radians per full revolution of wheels


    m1 = 0 #motor rpm values
    m2 = 0
    m3 = 0
    m4 = 0

    dx_max = max_rps*wheel_dist_per_rev #if all actuation resources are used for x movement
    dy_max = dx_max #inherently the same
    dphi_max = phi_rads_per_rev*max_rps #radians per second if all motors causing rotation

    dstates = np.matrix([[dx],[dy],[dphi]])
    kinematics_matrix = np.matrix([[1,0,outer_d/2],[0,1,outer_d/2],[-1,0,outer_d/2],[0,-1,outer_d/2]])/wheel_dist_per_rev*60 #local velocities to rpm
    motor_rpms = kinematics_matrix*dstates

    m1 = motor_rpms[0]
    m2 = motor_rpms[1]
    m3 = motor_rpms[2]
    m4 = motor_rpms[3]

#check for over actuation
    scale_factor = 1
    if(abs(m1) > 60 or abs(m2) > 60 or abs(m3) > 60 or abs(m4) > 60):
    #insert system notification for overactuation and rescaling so that
    #trajectory can be updated
        scale_factor = max_rpm/max(abs(m1),abs(m2),abs(m3),abs(m4))
        m1 = scale_factor*m1
        m2 = scale_factor*m2
        m3 = scale_factor*m3
        m4 = scale_factor*m4
    #this should allow for the same overall trajectory at overall slower speeds
    return [m1,m2,m3,m4,scale_factor] #return speeds with scale factor to acknowledge changes no scaling if =1

