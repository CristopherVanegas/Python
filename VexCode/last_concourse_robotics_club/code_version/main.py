#region VEXcode Generated Robot Configuration
import math
import random
from typing import ForwardRef
from vexcode import *

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()

# Library imports
from vexcode import *


# MAIN CODE - LOGIC
def main():
    drivetrain.set_turn_velocity(200, PERCENT)
    drivetrain.set_drive_velocity(200, PERCENT)
    move_to_one()
    move_to_three()
    move_to_four()
    move_to_two()
    move_to_start_point()



# VR threads — Do not delete
vr_thread(main())



# COMPETITION CODE
# DEFINITIONS FOR EACH MOVE

def move_to_one():
    # since base point -> green 1
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 475, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 165, MM)



def move_to_three():
    # since green 1 -> base point
    drivetrain.drive_for(REVERSE, 165, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 475, MM)
    
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)


    # since base point -> green 3
    for x in range(1, 12):
        module = x % 2
        if x == 1 or module != 0:
            if x == 9:
                drivetrain.turn_for(RIGHT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 470, MM)
                continue

            if x == 11:
                drivetrain.turn_for(RIGHT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 150, MM)
                continue
            
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 245, MM)
        
        elif module == 0:
            if x == 10:
                drivetrain.turn_for(RIGHT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 225, MM)
                continue
            
            drivetrain.turn_for(LEFT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 245, MM)



def move_to_four():
    # since green 3 -> green 4
    drivetrain.drive_for(REVERSE, 150, MM)
    
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 225, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 470, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 950, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 250, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 525, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 700, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 250, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 1200, MM)



def move_to_two():
    # since green 4 -> green 2
    drivetrain.drive_for(REVERSE, 1200, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 250, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 700, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 525, MM)

    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 250, MM)

    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 725, MM)
    
    for x in range(1, 6):
        if x % 2 == 0:
            if x == 4:
                drivetrain.turn_for(RIGHT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 225, MM)
                continue

            drivetrain.turn_for(LEFT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 225, MM)

        elif x % 2 != 0:
            if x == 1:
                drivetrain.turn_for(LEFT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 230, MM)
                continue

            if x == 5:
                drivetrain.turn_for(LEFT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 210, MM)
                continue

            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 245, MM)



def move_to_start_point():
    for x in range(1, 6):
        if x % 2 == 0:
            if x == 2:
                drivetrain.turn_for(LEFT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 525, MM)
                continue

            drivetrain.turn_for(LEFT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 245, MM)


        elif x % 2 != 0:
            if x == 1:
                drivetrain.drive_for(REVERSE, 225, MM)
                continue

            if x == 5:
                drivetrain.turn_for(RIGHT, 90, DEGREES)
                drivetrain.drive_for(FORWARD, 265, MM)
                continue
            
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 245, MM)
        
    drivetrain.turn_for(RIGHT, 180, DEGREES)
            
            





