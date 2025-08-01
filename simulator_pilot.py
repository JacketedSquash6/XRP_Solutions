import random
from utilities import NORTH, EAST, SOUTH, WEST, facing_left, facing_right, TURN_LEFT, TURN_RIGHT, FORWARD

class SimulatorPilot:        
    def __init__(self, dimensions):
        self.height = dimensions[0]
        self.width = dimensions[1]
        # Simulator ignores physical reality and places obstacles at random
        self.grid = [[(random.random() < 0.1) for j in range(self.width)] for i in range(self.height)] 

        self.robot_row = 0
        self.robot_col = 0
        self.robot_facing = NORTH

    def turn_left(self):
        self.robot_facing = facing_left(self.robot_facing)
        return True
    
    def turn_right(self):
        self.robot_facing = facing_right(self.robot_facing)
        return True
    
    def forward(self):
        if ((self.robot_facing == NORTH) and (self.robot_row == self.height-1) or
            (self.robot_facing == EAST) and (self.robot_col == self.width-1) or
            (self.robot_facing == SOUTH) and (self.robot_row == 0) or
            (self.robot_facing == WEST) and (self.robot_col == 0)):
            return False # Running into an outer wall
        
        if self.robot_facing == NORTH:
            (new_row, new_col) = (self.robot_row + 1, self.robot_col)
        elif self.robot_facing == EAST:
            (new_row, new_col) = (self.robot_row, self.robot_col + 1)
        elif self.robot_facing == SOUTH:
            (new_row, new_col) = (self.robot_row - 1, self.robot_col)
        elif self.robot_facing == WEST:
            (new_row, new_col) = (self.robot_row, self.robot_col - 1)
        else:
            raise RuntimeError("Robot does not have a legal facing")

        if self.grid[new_row][new_col]:
            return False # Running into an inner wall
        
        (self.robot_row, self.robot_col) = (new_row, new_col) # Update Position
        
        return True # Report successful movement
    
    def get_position(self):
        return (self.robot_row, self.robot_col)
    def get_facing(self):
        return self.robot_facing
    
    def do_actions(self, action_list):
        for action in action_list:
            if action == TURN_LEFT:
                result = self.turn_left()
            elif action == TURN_RIGHT:
                result = self.turn_right()
            elif action == FORWARD:
                result = self.forward()
            else:
                raise RuntimeError("Robot wants to do an undefined action")
            if result == False:
                return False

        return True

    def get_obstacles_list(self):
        obstacles = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == True:
                    obstacles.append((i,j))
        return obstacles