#!/usr/bin/env python

from robot import Robot
from kalman import KalmanFilter


if __name__ == '__main__':
    robot = Robot()
    filter = KalmanFilter(10.0, 10.0, 10.0, 10.0, 10.0, 10.0)

    for i in xrange(1000):
        robot.move(1.0)
        filter.update(1.0, robot.sensor())

        # Print the robot's actual position vs the filter estimate
        print robot.x, filter.mean

