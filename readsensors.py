#!/usr/bin/env micropython
"""Example usage of ev3devlight."""

from time import sleep
from ev3devlight.sensors import IRProximity, Gyro
from ev3devlight.brick import print_vscode

# Set up IR Sensor to detect objects
eyes = IRProximity('in4', threshold=20)

# Initialize a Gyro sensor
gyro = Gyro('in2')

# print the gyro value until the IR sensor sees something
while not eyes.detected:
    print_vscode(gyro.value)
    sleep(0.1)
