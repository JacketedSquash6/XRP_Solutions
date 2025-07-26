class Action:
    TURN_LEFT = 0
    TURN_RIGHT = 1
    FORWARD = 2
    DONE = 3

class Facing:
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
    
class Node:
    def __init__(self, row, col):
        self.position = (row, col)
        self.distance = None
        self.visited = False
        self.previous = None
        
def bfs(map, start, end):
    # unrolling position tuples
    start_row, start_col = start 
    end_row, end_col = end
    # extracting the height and width of the grid by looking at the map list's dimensions
    height = len(map)
    width = len(map[0])

    # initializing the array of nodes with their positions
    nodes = [[Node(j, i) for i in range(width)] for j in range(height)]
    nodes[start_row][start_col].distance = 0
    nodes[start_row][start_col].visited = True

    for i in range(width * height): # we want to iterate through all 0-distance nodes to find all 1-distance nodes, then through 1s to find 2s, etc.
        #  A good upper bound for distance is width*height because there are only that many nodes total. In general, we will find the endpoint much sooner than that and break out
        for row in range(height):
            for col in range(width):
                if map[row][col] == True:
                    continue # Locations that are blocked do not need to be considered

                node = nodes[row][col]
                if node.visited: # a visited node has already been assigned a distance, so we don't need to look at it again
                    continue

                neighbors = []
                if row < height-1: # if we are not at the top, then there is a node above us
                    neighbors.append(nodes[row+1][col])
                if row > 0: # if we are not at the bottom, then there is a node below us
                    neighbors.append(nodes[row-1][col])
                if col < width-1: # if we are not at the rightmost column, then there is a node to the right
                    neighbors.append(nodes[row][col+1])
                if col > 0: # if we are not at the leftmost column, then there is a node to the left
                    neighbors.append(nodes[row][col-1])

                for neighbor in neighbors: # we need to check all four neighbors to see if they have the right distance
                    if neighbor.distance == i:
                        node.distance = i+1
                        node.visited = True
                        node.previous = neighbor
                        break
    output = []
    predecessor = nodes[end_row][end_col]
    while predecessor.previous is not None:
        output.insert(0, predecessor.position)
        predecessor = predecessor.previous
    return output    