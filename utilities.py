TURN_LEFT = 0
TURN_RIGHT = 1
FORWARD = 2

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def facing_left(f):
    if f == NORTH:
        return WEST
    if f ==  EAST:
        return NORTH
    if f == SOUTH:
        return EAST
    if f == WEST:
        return SOUTH
def facing_right(f):
    if f == NORTH:
        return EAST
    if f == EAST:
        return SOUTH
    if f == SOUTH:
        return WEST
    if f == WEST:
        return NORTH
def facing_opposite(f):
    if f == NORTH:
        return SOUTH
    if f == EAST:
        return WEST
    if f == SOUTH:
        return NORTH
    if f == WEST:
        return EAST