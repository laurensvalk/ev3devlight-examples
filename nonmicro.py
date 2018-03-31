#!/usr/bin/env python3
"""Example usage of ev3devlight library without micropython."""

from time import sleep

# Tell python3 where to find ev3devlight
import sys
sys.path.append('/home/robot/.micropython/lib/ev3devlight')

from ev3devlight.sensors import Touch

# Set up Touch Sensor to detect objects
button = Touch('in1')

# print the gyro value until the IR sensor sees something
while not button.pressed:
    sleep(0.1)
