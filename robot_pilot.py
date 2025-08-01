from XRPLib.defaults import *
from utilities import NORTH, EAST, SOUTH, WEST, facing_left, facing_right, TURN_LEFT, TURN_RIGHT, FORWARD

BASE_EFFORT = 0.3
TURN_CONSTANT = 0.5

class RobotPilot:
    def __init__(self):
        self.robot_row = 0
        self.robot_col = 0
        self.robot_facing = NORTH

    def turn_left(self):
        drivetrain.turn(80)
        while reflectance.get_right()<0.8:
               drivetrain.set_effort(-0.3,0.3)
        self.robot_facing = facing_left(self.robot_facing)
    
    def turn_right(self): 
        drivetrain.turn(-80)
        while reflectance.get_left()<0.8:
               drivetrain.set_effort(0.3,-0.3)
        self.robot_facing = facing_right(self.robot_facing)
    
    def forward(self):
        while True:
            self.line_follow()
            if self.check_intersection():
                drivetrain.straight(10)
                break
        
        if self.robot_facing == NORTH:
            self.robot_row = self.robot_row + 1
        elif self.robot_facing == EAST:
            self.robot_col = self.robot_col + 1
        elif self.robot_facing == SOUTH:
            self.robot_row = self.robot_row - 1
        elif self.robot_facing == WEST:
            self.robot_col = self.robot_col - 1
    
    def get_position(self):
        return (self.robot_row, self.robot_col)
    def get_facing(self):
        return self.robot_facing
    def do_actions(self, action_list):
        for action in action_list:
            if action == TURN_LEFT:
                self.turn_left()
            elif action == TURN_RIGHT:
                self.turn_right()
            elif action == FORWARD:
                self.forward()
            else:
                raise RuntimeError("Robot wants to do an undefined action")
        
    # Helper Functions
    def line_follow(self):
        turn_offset = TURN_CONSTANT * (reflectance.get_left() - reflectance.get_right())
        drivetrain.set_effort(BASE_EFFORT - turn_offset, BASE_EFFORT + turn_offset)
    def check_intersection(self):
        return (reflectance.get_left()>0.81 and reflectance.get_right()>0.81)