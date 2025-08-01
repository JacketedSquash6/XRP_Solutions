from utilities import Node

class BFSPlanner:
    def __init__(self, dimensions, obstacles):
        self.height = dimensions[0]
        self.width = dimensions[1]
        self.obstacles = obstacles

    def plan(self, start, end):
        # unrolling position tuples
        start_row, start_col = start 
        end_row, end_col = end

        # initializing the array of nodes with their positions
        nodes = [[Node(j, i) for i in range(self.width)] for j in range(self.height)]
        nodes[start_row][start_col].distance = 0
        nodes[start_row][start_col].visited = True

        for i in range(self.width * self.height): # we want to iterate through all 0-distance nodes to find all 1-distance nodes, then through 1s to find 2s, etc.
            #  A good upper bound for distance is width*height because there are only that many nodes total. In general, we will find the endpoint much sooner than that and break out
            for row in range(self.height):
                for col in range(self.width):
                    if (row, col) in self.obstacles:
                        continue # Locations that are blocked do not need to be considered

                    node = nodes[row][col]
                    if node.visited: # a visited node has already been assigned a distance, so we don't need to look at it again
                        continue

                    neighbors = []
                    if row < self.height-1: # if we are not at the top, then there is a node above us
                        neighbors.append(nodes[row+1][col])
                    if row > 0: # if we are not at the bottom, then there is a node below us
                        neighbors.append(nodes[row-1][col])
                    if col < self.width-1: # if we are not at the rightmost column, then there is a node to the right
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
        while predecessor is not None:
            output.insert(0, predecessor.position)
            predecessor = predecessor.previous
        return output