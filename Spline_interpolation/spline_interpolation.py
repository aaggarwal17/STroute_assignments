# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:09:18 2017

@author: user
"""

def finding_velocity(n):
    start_time = pre_time[i-1]
    end_time = pre_time[i]
    start_speed = pre_velocity[i-1]
    end_speed = pre_velocity[i]
    
    found_velocity = (start_speed) + ((end_speed - start_speed) * 
    (n - start_time)) / (end_time - start_time)
    
    return found_velocity
#######################################################
global pre_time
global pre_velocity


pre_time = [0, 10, 15, 20, 22.5]
pre_velocity = [0, 227.04, 362.78, 517.35, 602.97]

#######################################################
print "Enter the time: "
n = int(input())
find_time = n
#######################################################

if find_time in pre_time:
    ixd = pre_time.index(find_time)
    print ("The velocity for " +str(find_time)+ "'s is: ")
    print (str(pre_velocity[ixd])+"m/s")   
    
else:
    i = 0
    for x in pre_time:
    
        if (find_time > x):
            i += 1
            break
    print ("The velocity for " +str(find_time)+ "'s is: ")
    print (str(finding_velocity(n))+"m/s") 
    