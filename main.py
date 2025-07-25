import random
from XRPLib.defaults import *

BASE_EFFORT = 0.3
TURN_CONSTANT = 0.5

height = 6
width = 6

targets = []
for i in range(10):
    t_row = random.randint(0, height-1)
    t_col = random.randint(0, width-1)
    targets.append((t_row, t_col))

position = (0, 0)

for target in targets:
    ### We need to go some number of spaces North or South depending on the difference between ourselves and our target

    vertical = target[0] - position[0]
    if vertical < 0:
        # if we need to drive south, turn around
        turn_left()
        turn_left()
    # the absolute value tells you how many intersections to go forward
    for i in range(abs(vertical)):
        forward()
    if vertical < 0:
        # we are facing south, and the following code will assume that we're facing North, so let's turn back North.
        # if you're clever, you can avoid this extra turning, but you have to be careful to keep track of which way you're facing
        turn_left()
        turn_left()
    
    ### Now we're on the right row. Let's get to the right column

    horizontal = target[1] - position[1]
    # turn left or right depending on which way we need to go
    if horizontal < 0:
        turn_left()
    else: 
        turn_right()
    
    # travel forward
    for i in range(abs(horizontal)):
        forward()
    
    # turn back to face North for the next cycle
    if horizontal < 0:
        turn_right()
    else: 
        turn_left()

        

def turn_left(self):
    drivetrain.turn(80)
    while reflectance.get_right()<0.8:
            drivetrain.set_effort(-BASE_EFFORT, BASE_EFFORT)
            
    return True

def turn_right(self): 
    drivetrain.turn(-80)
    while reflectance.get_left()<0.8:
            drivetrain.set_effort(BASE_EFFORT, -BASE_EFFORT)

    return True

def forward(self):
    while True:
        self.line_follow()
        if self.check_intersection():
            drivetrain.straight(10)
            break

    return True

def line_follow(self):
    turn_offset = TURN_CONSTANT * (reflectance.get_left() - reflectance.get_right())
    drivetrain.set_effort(BASE_EFFORT - turn_offset, BASE_EFFORT + turn_offset)
    
def check_intersection(self):
    return (reflectance.get_left()>0.81 and reflectance.get_right()>0.81)