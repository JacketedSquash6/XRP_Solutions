from XRPLib.defaults import *

BASE_SPEED = 0.25
GAIN = 0.3

def line_follow(self):
    left_reflectance = reflectance.get_left()
    right_reflectance = reflectance.get_right()
    turn_offset = GAIN * (left_reflectance - right_reflectance)
    drivetrain.set_effort(BASE_SPEED - turn_offset, BASE_SPEED + turn_offset)

def check_intersection(self):
    return (reflectance.get_left()>0.81 and reflectance.get_right()>0.81)

def turn_around(self):
    drivetrain.turn(175)
    while reflectance.get_right()<0.8:
            drivetrain.set_effort(-BASE_SPEED, BASE_SPEED)

while True:
    self.line_follow()
    if self.check_intersection():
        turn_around()