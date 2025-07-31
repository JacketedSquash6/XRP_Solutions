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


def display(grid, robot_position, robot_facing):
    height = len(grid)
    width = len(grid[0])
    print("-----------------")
    for i in range(height-1, -1, -1): # Since we are printing top-to-bottom but the positive y direction is north, we must print the lines in reverse order
        for j in range(width):
            if i  == robot_position[0] and j == robot_position[1]:
                if robot_facing == NORTH:
                    char = '^'
                elif robot_facing == EAST:
                    char = '>'
                elif robot_facing == SOUTH:
                    char = 'V'
                elif robot_facing == WEST:
                    char = '<'
                else:
                    raise RuntimeError("Robot does not have a legal facing")
            elif grid[i][j] == True:
                char = '#'
            else:
                char = '.'
            print(char, end=' ')
        print()