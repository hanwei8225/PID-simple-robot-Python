#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :
@Description    :
@Time           :
@Author         :frank
@Version        :1.0
'''

from robot import Robot
from matplotlib import pyplot as plt
import math


y1 = []
y2 = []

def run(params, printflag = False):
    myrobot = Robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0
    err = 0
    N =100
    myrobot.set_steering_drift(10.0/180.0 * math.pi)
    crosstrack_error = 1.0
    int_crosstalk_error = 0.0
    delta_t = 1
    for i in range(N * 2):
        diff_crosstalk_error = myrobot.y - crosstrack_error
        crosstrack_error = myrobot.y
        int_crosstalk_error += crosstrack_error
        steer = -params[0] * crosstrack_error - params[1] * diff_crosstalk_error - params[2] *int_crosstalk_error
        myrobot.move(steer, speed)
        if i > N:
            err += (crosstrack_error ** 2)
        if printflag:
            print(myrobot,steer / math.pi * 180.0)
    return err / float(N)


def twiddle(tol=0.2):
    n_params = 3

    p = [0.0 for x in range(n_params)]
    dp = [1.0 for x in range(n_params)]
    # dp[1] = 0
    best_err = run(p)
    n = 0
    while sum(dp) > tol:
        for i in range(n_params):
            p[i] += dp[i]
            err = run(p)
            if err < best_err:
                best_err = err
                dp[i] *= 1.1
            else:
                p[i] -= dp[i] * 2
                err = run(p)
                if err < best_err:
                    best_err = err
                    dp[i] *= 1.1
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.9
        n += 1
        print("Twiddle #", n, p, "-> ", best_err)
        y1.append(best_err)
        y2.append(p)
    return p


params = twiddle(0.01)

err = run(params)

print("final params :", params, "err -> ", err)
plt.plot(y1)
plt.show()


