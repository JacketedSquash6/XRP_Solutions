from XRPLib.defaults import *
from utilities import TURN_LEFT, TURN_RIGHT, FORWARD

BASE_EFFORT = 0.3
TURN_CONSTANT = 0.5

class RobotPilot:
    def turn_left(self):
        drivetrain.turn(80)
        while reflectance.get_right()<0.8:
               drivetrain.set_effort(-0.3,0.3)
    
    def turn_right(self): 
        drivetrain.turn(-80)
        while reflectance.get_left()<0.8:
               drivetrain.set_effort(0.3,-0.3)
    
    def forward(self):
        while True:
            self.line_follow()
            if self.check_intersection():
                drivetrain.straight(10)
                break
    
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