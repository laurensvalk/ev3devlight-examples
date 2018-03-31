#!/usr/bin/env micropython
"""Example usage of ev3devlight."""

from time import sleep
from ev3devlight.sensors import Proximity, Gyro, Remote
from ev3devlight.brick import print_vscode, Battery

# Set up IR Sensor to detect objects
eyes = Proximity('in4', threshold=20)

# Initialize a Gyro sensor
gyro = Gyro('in2', read_rate=True, read_angle=False)

# print the gyro value until the IR sensor sees something
while not eyes.detected:
    print_vscode(gyro.rate)
    sleep(0.1)

print_vscode("Press IR button to end program")

# Set infrared sensor in remote mode
commander = Remote('in4')

# Battery diagnostics
supply = Battery()

while commander.pressed('NONE'):
    print_vscode(supply.voltage)
    sleep(0.1)
