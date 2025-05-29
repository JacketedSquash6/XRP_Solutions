from enum import Enum

class Action(Enum):
    TURN_LEFT = 0
    TURN_RIGHT = 1
    FORWARD = 2
    DONE = 3 # TODO Leave this out in the initial code, so that students can come up with the fact that they need a new function

class Facing(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    def left(f):
        if f == Facing.NORTH:
            return Facing.WEST
        if f == Facing.EAST:
            return Facing.NORTH
        if f == Facing.SOUTH:
            return Facing.EAST
        if f == Facing.WEST:
            return Facing.SOUTH
    def right(f):
        if f == Facing.NORTH:
            return Facing.EAST
        if f == Facing.EAST:
            return Facing.SOUTH
        if f == Facing.SOUTH:
            return Facing.WEST
        if f == Facing.WEST:
            return Facing.NORTH

class Pilot:
    def __init__(self):
        pass

    def turn_right(self):
        return True
    
    def turn_left(self):
        return True

    def forward(self):
        return True
    
    def test_target(self, target):
        return False

class Navigator:
    def __init__(self, position = (0,0), facing = Facing.NORTH, map = [[False for i in range(6)] for j in range(6)]):
        self.my_row = position[0]
        self.my_col = position[1]
        self.my_facing = facing
        self.map = map

    def set_target(self, target):
        self.target_row = target[0]
        self.target_col = target[1]
    
    def select_action(self):
        return Action.FORWARD
    
class Node:
    def __init__(self, row, col):
        self.position = (row, col)
        self.distance = None
        self.visited = False
        self.previous = None