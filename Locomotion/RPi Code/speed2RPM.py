import numpy
#####################################################################
# motor layout                 +1-                                  #
#                         -           +                             #
# >x+                     2           4                             #
# ^y+                     +           -                             #
# phi ccw+                     -3+                                  #
#####################################################################
def  speed2RPM(dx,dy,dphi):
    wheel_d = .1524 #wheel diameter in meters (6")
    wheel_dist_per_rev = wheel_d*pi
    outer_d = .6096 #diameter of outer robot in meters (2')

    min_rpm = 0 #to be updated if I find if there is an actuation minimum
    max_rpm = 60 #to be determined experimentally. Spec sheet 80rpm
    max_rps = max_rpm/60 #slightly more useful in calculations
    phi_rads_per_rev = wheel_dist_per_rev/(outer_d/2) #phi radians per full revolution of wheels


    m1 = 0 #motor rpm values
    m2 = 0
    m3 = 0
    m4 = 0

    dx   = 0 #in m/s
    dy   = 0 #in m/s
    dphi = 0 #in rad/s

#create input in form dx,dy,dphi if made into function

    dx_max = max_rps*dist_per_rev #if all actuation resources are used for x movement
    dy_max = dx_max #inherently the same
    dphi_max = phi_rads_per_rev*max_rps #radians per second if all motors causing rotation

#create a decoder for dx dy dphi to m1 m2 m3 m4

#first need to allocate for dx and dy, which are completely independent

    m3_x = dx/wheel_dist_per_rev*60
    m1_x = -m3_x

    m4_y = dy/wheel_dist_per_rev*60
    m2_y = -m4_y

#now need to calculate phi component

    m1_phi = dphi/phi_rads_per_rev*60
    m2_phi = dphi/phi_rads_per_rev*60
    m3_phi = dphi/phi_rads_per_rev*60
    m4_phi = dphi/phi_rads_per_rev*60

#combine all together

    m1 = m1_x + m1_phi
    m2 = m2_y + m2_phi
    m3 = m3_x + m3_phi
    m4 = m4_y + m4_phi

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
