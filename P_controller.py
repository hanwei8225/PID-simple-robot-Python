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


x = []
y = []

def run(param):
    myrobot = Robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0
    N =1000
    for i in range(N):
        crosstrack_error = myrobot.y
        steering = -crosstrack_error * param
        myrobot.move(steering, speed)
        y.append(myrobot.y)
        print(myrobot, "steering =", steering)


run(0.1)
plt.plot(y)
plt.show()