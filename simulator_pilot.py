from templates import Facing, Pilot


class SimulatorPilot(Pilot):        
    def __init__(self, map):
        self.height = len(map)
        self.width = len(map[0])
        self.map = map

        self.robot_row = 0
        self.robot_col = 0
        self.robot_facing = Facing.NORTH

    ## Mandatory Functions
    def turn_left(self):
        self.robot_facing = Facing.left(self.robot_facing)
        
        return True
    
    def turn_right(self):
        self.robot_facing = Facing.right(self.robot_facing)
        
        return True
    
    def forward(self):
        if ((self.robot_facing == Facing.NORTH) and (self.robot_row == self.height-1) or
            (self.robot_facing == Facing.EAST) and (self.robot_col == self.width-1) or
            (self.robot_facing == Facing.SOUTH) and (self.robot_row == 0) or
            (self.robot_facing == Facing.WEST) and (self.robot_col == 0)):
            return False # Running into an outer wall
        
        if self.robot_facing == Facing.NORTH:
            (new_row, new_col) = (self.robot_row + 1, self.robot_col)
        elif self.robot_facing == Facing.EAST:
            (new_row, new_col) = (self.robot_row, self.robot_col + 1)
        elif self.robot_facing == Facing.SOUTH:
            (new_row, new_col) = (self.robot_row - 1, self.robot_col)
        elif self.robot_facing == Facing.WEST:
            (new_row, new_col) = (self.robot_row, self.robot_col - 1)
        else:
            raise RuntimeError("Agent does not have a legal facing")

        if self.map[new_row][new_col]:
            return False # Running into an inner wall
        
        (self.robot_row, self.robot_col) = (new_row, new_col) # Update Position
        
        return True # Report successful movement
    
    def test_target(self, target):
        return (self.robot_row == target[0] and self.robot_col == target[1])
    
    ## Helper Functions
    def get_map(self):
        return self.map

    def char_at(self, row, col): # TODO Have students write this themselves. Maybe as an extra credit opportunity, make it modular so they can use the Turtle module to make a more graphical visualization of the situation
        if self.robot_row == row and self.robot_col == col:
            if self.robot_facing == Facing.NORTH:
                return '^'
            elif self.robot_facing == Facing.EAST:
                return '>'
            elif self.robot_facing == Facing.SOUTH:
                return 'V'
            elif self.robot_facing == Facing.WEST:
                return '<'
            else:
                raise RuntimeError("Agent does not have a legal facing")
        elif self.map[row][col]:
            return '#'
        else:
            return '.'

    def display(self):
        print("-----------------")
        for i in range(self.height-1, -1, -1):
            for j in range(self.width):
                print(self.char_at(i, j), end=' ')
            print()