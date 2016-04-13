#!/usr/bin/env python

from robot import Robot
from kalman import KalmanFilter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

x_real = [0]*1000
x_filter = [0]*1000

if __name__ == '__main__':
    '''
    robot = Robot(0.0,0.0,0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, 0.0, 1.0, 1.0)
    for i in xrange(1000):
        robot.move(1.0)
        filter.update(1.0, robot.sensor())
        x_real[i] = robot.x
        x_filter[i] = filter.mean

    plt.figure(1)
    plt.title('Perfect movement and perfect sensing')
    plt.plot(x_real,label = 'Actual position')
    plt.plot(x_filter,label = 'Filter estimate')
    plt.xlabel("time")
    plt.ylabel("x - robot's position")
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)
    
'''

    robot = Robot(1.0,1.0,0.0)
    filter = KalmanFilter(1.0, 2.0, 1.0, 0.0, 1.0)
    for i in xrange(1000):
        robot.move(1.0)
        filter.update(1.0, robot.sensor())
        x_real[i] = robot.x
        x_filter[i] = filter.mean
        
    plt.figure(2)
    plt.title('large variance of movement and sensor models')
    plt.plot(x_real,label = 'Actual position')
    plt.plot(x_filter,label = 'Filter estimate')
    plt.xlabel("time")
    plt.ylabel("x - robot's position")
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)

    '''
    robot = Robot(0,10.0,0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, 0.0, 1.0, 1.0)
    for i in xrange(1000):
        robot.move(1.0)
        filter.update(1.0, robot.sensor())
        x_real[i] = robot.x
        x_filter[i] = filter.mean
    plt.figure(3)
    plt.title('Incorrect mevement')
    plt.plot(x_real,label = 'Actual position')
    plt.plot(x_filter,label = 'Filter estimate')
    plt.xlabel("time")
    plt.ylabel("x - robot's position")
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)

    robot = Robot(100,0.0,0.0)
    filter = KalmanFilter(1.0, 1.0, 1.0, 0.0, 1.0, 1.0)
    for i in xrange(1000):
        robot.move(1.0)
        filter.update(1.0, robot.sensor())
        x_real[i] = robot.x
        x_filter[i] = filter.mean
    plt.figure(4)
    plt.title('Incorrect sensor model')
    plt.plot(x_real,label = 'Actual position')
    plt.plot(x_filter,label = 'Filter estimate')
    plt.xlabel("time")
    plt.ylabel("x - robot's position")
    plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=1.)
    '''
    plt.show()
