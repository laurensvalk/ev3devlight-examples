#!/usr/bin/env micropython
"""Example script that can run on either an EV3 or a PC.

On the EV3, it makes a robot drive forwards.
On the PC, it generates dummy hardware files and does nothing else.

This is useful for debugging complex algorithms quickly on a PC.
Anything related to the EV3 hardware is effectively ignored.
"""
# Regular imports for our robot
from ev3devlight.motors import DriveBase
from time import sleep

# These lines check if the code is being executed on an EV3
# If not, dummy files are generated in the local directory,
# so that the code can run on the EV3 even though there are
# no motors or sensors.
from ev3devlight.fileio import real_robot
if not real_robot():
    from ev3devlight.virtualhardware import make_files
    make_files()

# Set up a drivebase from two motors
base = DriveBase(left_port='outB',
                 right_port='outC',
                 wheel_diameter=3.5,
                 wheel_span=14.5)

# Make it move with a speed (cm/s) and turnrate (deg/s)
base.drive_and_turn(3, 0)

# Sleep
sleep(1)

# Stop the base
base.stop()
