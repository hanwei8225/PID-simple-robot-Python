#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :
@Description    :
@Time           :
@Author         :frank
@Version        :1.0
'''

from robot1 import Robot
from matplotlib import pyplot as plt
import math



y = []

def run(param1,param2):
    myrobot = Robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0
    N =1000
    myrobot.set_steering_drift(10.0/180.0 * math.pi)
    crosstrack_error = myrobot.y
    delta_t = 1
    for i in range(N):
        diff_crosstalk_error = myrobot.y - crosstrack_error
        crosstrack_error = myrobot.y
        steering = -crosstrack_error * param1 - param2 * diff_crosstalk_error / delta_t
        myrobot.move(steering, speed)
        y.append(myrobot.y)
        print(myrobot, "steering =", steering)


run(0.2, 3.0)
plt.plot(y)
plt.show()