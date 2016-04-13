#!/usr/bin/env python

from robot import Robot
from kalman import KalmanFilter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

num = 100
x_real = [0]*num
x_sensor = [0]*num
x_filter = [0]*num
x_filter2 = [0]*num
x_filter3 = [0]*num
x_filter4 = [0]*num

if __name__ == '__main__':
    
    # Question 1 -------------------------------------------------------
    robot = Robot(0.0,0.0,0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, \
                             1.0, 1.0,\
                             0.0,10.0)
    for i in xrange(num):
        speed  = 1.0 - (float(i)/float(num))
        robot.move(speed)
        x_sensor[i] = robot.sensor()
        filter.update(speed, x_sensor[i])
        x_real[i] = robot.x
        x_filter[i] = filter.mean

    plt.figure(1,figsize=(12, 8))
    plt.title('Perfect movement and perfect sensing (var_move=0, var_sensor=0)')
    plt.plot(x_real,label = 'Actual position',lw = 2)
    plt.plot(x_sensor, 'r--',label = 'Observations')
    plt.plot(x_filter,label = 'Filter estimate')
    plt.xlabel("time")
    plt.ylabel("x - robot's position")
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)
 
    # Question 2 -------------------------------------------------------
    robot = Robot(5.0, 0.2, 0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, \
                             0.002, 0.1,\
                             0.0,10.0)
    filter2 = KalmanFilter(1.0, 1.0, 1.0, \
                             0.02, 0.1,\
                             0.0,10.0)
    filter3 = KalmanFilter(1.0, 1.0, 1.0, \
                             0.2, 0.1,\
                             0.0,10.0)
    for i in xrange(num):
        speed  = 1.0 - (float(i)/float(num))
        robot.move(speed)
        x_sensor[i] = robot.sensor()
        filter.update(speed, x_sensor[i])
        filter2.update(speed, x_sensor[i])
        filter3.update(speed, x_sensor[i])
        x_real[i] = robot.x
        x_filter[i] = filter.mean
        x_filter2[i] = filter2.mean
        x_filter3[i] = filter3.mean
    plt.figure(2,figsize=(12, 8))
    plt.plot(x_real,label = 'Actual position',lw = 2)
    plt.plot(x_sensor, 'r--',label = 'Observations')
    plt.plot(x_filter,label = 'Filter estimate(q = 0.002,r = 1.0)',lw = 2)
    plt.plot(x_filter2,label = 'Filter estimate(q = 0.02,r = 1.0)')
    plt.plot(x_filter3,label = 'Filter estimate(q = 0.2,r = 1.0)')
    plt.title('Increase the variance of the movement in KF (var_move=0.2, var_sensor=5.0)')
    plt.xlabel("time")
    plt.ylabel("x")
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=1.)

    robot = Robot(5.0, 0.2, 0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, \
                             0.2, 0.05,\
                             0.0,10.0)
    filter2 = KalmanFilter(1.0, 1.0, 1.0, \
                             0.2, 0.5,\
                             0.0,10.0)
    filter3 = KalmanFilter(1.0, 1.0, 1.0, \
                             0.2, 5,\
                             0.0,10.0)
    for i in xrange(num):
        speed  = 1.0 - (float(i)/float(num))
        robot.move(speed)
        x_sensor[i] = robot.sensor()
        filter.update(speed, x_sensor[i])
        filter2.update(speed, x_sensor[i])
        filter3.update(speed, x_sensor[i])
        x_real[i] = robot.x
        x_filter[i] = filter.mean
        x_filter2[i] = filter2.mean
        x_filter3[i] = filter3.mean
    plt.figure(3,figsize=(12, 8))
    plt.plot(x_real,label = 'Actual position',lw = 2)
    plt.plot(x_sensor, 'r--',label = 'Observations')
    plt.plot(x_filter,label = 'Filter estimate(q = 0.2,r = 0.05)')
    plt.plot(x_filter2,label = 'Filter estimate(q = 0.2,r = 0.5)')
    plt.plot(x_filter3,label = 'Filter estimate(q = 0.2,r = 5.0)',lw = 2)
    plt.title('Increase the variance of the sensor model in KF (var_move=0.2, var_sensor=5.0)')
    plt.xlabel("time")
    plt.ylabel("x")
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=1.)


    # Question 3 -------------------------------------------------------
    robot = Robot(5.0, 0.2, 0.0)
    filter = KalmanFilter(2.0, 1.0, 1.0, \
                             0.2, 5,\
                             0.0,10.0)
    filter2 = KalmanFilter(1.0, 2.0, 1.0, \
                             0.2, 5,\
                             0.0,10.0)
    filter3 = KalmanFilter(1.0, 1.0, 2.0, \
                             0.2, 5,\
                             0.0,10.0)
    for i in xrange(num):
        speed  = 1.0 - (float(i)/float(num))
        robot.move(speed)
        x_sensor[i] = robot.sensor()
        filter.update(speed, x_sensor[i])
        filter2.update(speed, x_sensor[i])
        filter3.update(speed, x_sensor[i])
        x_real[i] = robot.x
        x_filter[i] = filter.mean
        x_filter2[i] = filter2.mean
        x_filter3[i] = filter3.mean
    plt.figure(4,figsize=(12, 8))
    plt.plot(x_real,label = 'Actual position',lw = 2)
    plt.plot(x_sensor, 'r--',label = 'Observations')
    plt.plot(x_filter,label = 'Filter estimate(a=2, b=1,c=1)')
    plt.plot(x_filter2,label = 'Filter estimate(a=1, b=2,c=1)',lw = 2)
    plt.plot(x_filter3,label = 'Filter estimate(a=1, b=1,c=2)')
    plt.title('Incorrect movement or the sensor model in KF (var_move=0.2, var_sensor=5.0)')
    plt.xlabel("time")
    plt.ylabel("x")
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=1.)


    # Question 4 -------------------------------------------------------
    robot = Robot(10.0, 2.0, 0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, \
                             2, 10,\
                             0.0,10.0)
    filter2 = KalmanFilter(1.0, 1.0, 1.0, \
                             0.002, 10,\
                             0.0,10.0)
    filter3 = KalmanFilter(1.0, 1.0, 1.0, \
                             2, 0.01,\
                             0.0,10.0)
    for i in xrange(num):
        speed  = 1.0 - (float(i)/float(num))
        robot.move(speed)
        x_sensor[i] = robot.sensor()
        filter.update(speed, x_sensor[i])
        filter2.update(speed, x_sensor[i])
        filter3.update(speed, x_sensor[i])
        x_real[i] = robot.x
        x_filter[i] = filter.mean
        x_filter2[i] = filter2.mean
        x_filter3[i] = filter3.mean
    plt.figure(5,figsize=(12, 8))
    plt.plot(x_real,label = 'Actual position',lw = 2)
    plt.plot(x_sensor, 'r--',label = 'Observations')
    plt.plot(x_filter,label = 'Filter estimate(q=2.0, r=10.0)',lw = 2)
    plt.plot(x_filter2,label = 'Filter estimate(q=0.002, r=10.0)')
    plt.plot(x_filter3,label = 'Filter estimate(q=1.0, r=0.01)')
    plt.title('optimal parameters in KF (var_move=2.0, var_sensor=10.0)')
    plt.xlabel("time")
    plt.ylabel("x")
    plt.legend(bbox_to_anchor=(1, 0), loc=4, borderaxespad=1.)



    plt.show()
