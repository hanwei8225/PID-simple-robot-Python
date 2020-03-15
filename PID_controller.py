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

def run(param1,param2,param3):
    myrobot = Robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0
    N =100
    myrobot.set_steering_drift(10.0/180.0 * math.pi)
    crosstrack_error = myrobot.y
    int_crosstalk_error = 0
    delta_t = 1
    for i in range(N):
        diff_crosstalk_error = myrobot.y - crosstrack_error
        crosstrack_error = myrobot.y
        int_crosstalk_error += crosstrack_error
        steering = -crosstrack_error * param1 - param2 * diff_crosstalk_error / delta_t -param3 * int_crosstalk_error
        myrobot.move(steering, speed)
        y.append(myrobot.y)
        print(myrobot, "steering =", steering)


run(2.195279127584432, 8.71639967501516, 0.24370616448808052)
plt.plot(y)
plt.show()