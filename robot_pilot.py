from XRPLib.defaults import *
from templates import Facing, Pilot

BASE_EFFORT = 0.3
TURN_CONSTANT = 0.5

class RobotPilot(Pilot):
    def turn_left(self):
        drivetrain.turn(80)
        while reflectance.get_right()<0.8:
               drivetrain.set_effort(-0.3,0.3)
               
        return True
    
    def turn_right(self): 
        drivetrain.turn(-80)
        while reflectance.get_left()<0.8:
               drivetrain.set_effort(0.3,-0.3)

        return True
    
    def forward(self):
        while True:
            self.line_follow()
            if self.check_intersection():
                drivetrain.straight(10)
                break

        return True
        
    def test_target(self, target):
        return False
        
    def line_follow(self):
        turn_offset = TURN_CONSTANT * (reflectance.get_left() - reflectance.get_right())
        drivetrain.set_effort(BASE_EFFORT - turn_offset, BASE_EFFORT + turn_offset)
    def check_intersection(self):
        return (reflectance.get_left()>0.81 and reflectance.get_right()>0.81)