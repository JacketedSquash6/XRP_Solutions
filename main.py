from XRPLib.defaults import *

### 1.
# while True:
#     print(reflectance.get_left(), reflectance.get_right())


### 2.
BASE_SPEED = 0.25
GAIN = 0.3

def line_follow(self):
    left_reflectance = reflectance.get_left()
    right_reflectance = reflectance.get_right()
    turn_offset = GAIN * (left_reflectance - right_reflectance)
    drivetrain.set_effort(BASE_SPEED - turn_offset, BASE_SPEED + turn_offset)

while True:
    line_follow()
