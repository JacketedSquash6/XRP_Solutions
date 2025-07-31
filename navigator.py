from utilities import NORTH, EAST, SOUTH, WEST, facing_left, facing_right, facing_opposite, TURN_LEFT, TURN_RIGHT, FORWARD

class Node:
    def __init__(self, row, col):
        self.position = (row, col)
        self.distance = None
        self.visited = False
        self.previous = None

class Navigator:
    def navigate_to(grid, position, facing, target):
        node_list = Navigator.bfs(grid, position, target)
        action_list = Navigator.generate_actions(node_list, facing)
        return action_list

    def generate_actions(node_list, initial_facing):
        action_list = [] # This is what we will return
        current_row = node_list[0][0] # Our initial position is the first item in the node chain
        current_col = node_list[0][1]
        node_list.pop(0)
        current_facing = initial_facing # Our initial facing is given

        while len(node_list) > 0:
            next_row = node_list[0][0] # At any given moment, the next position we have to navigate to will be at the front of the list
            next_col = node_list[0][1]

            # Based on where we're going, decide which way we need to face
            if next_row == current_row + 1 and next_col == current_col: 
                next_facing = NORTH
            elif next_row == current_row and next_col == current_col + 1:
                next_facing = EAST
            elif next_row == current_row - 1 and next_col == current_col:
                next_facing = SOUTH
            elif next_row == current_row and next_col == current_col - 1:
                next_facing = WEST
            else:
                raise RuntimeError("Navigator wants to move to a non-adjacent space")
            
            # Based on which way we have to face to get where we're going, add different instructions to the list
            if next_facing == current_facing:
                action_list.append(FORWARD)
            elif next_facing == facing_left(current_facing):
                action_list.append(TURN_LEFT)
                action_list.append(FORWARD)
            elif next_facing == facing_right(current_facing):
                action_list.append(TURN_RIGHT)
                action_list.append(FORWARD)
            elif next_facing == facing_opposite(current_facing):
                # action_list.append(TURN_AROUND) # If there is a turn_around function, it is equally appropriate to call it instead of two 90degree turns
                action_list.append(TURN_LEFT)
                action_list.append(TURN_LEFT)
                action_list.append(FORWARD)
            else:
                raise RuntimeError("Navigator has invalid facing")
            
            # After executing the queued instructions, the robot will be at a new position and facing. We update this for future computations
            current_facing = next_facing
            current_row = next_row
            current_col = next_col
            node_list.pop(0)
        
        return action_list


    def bfs(grid, start, end):
        # unrolling position tuples
        start_row, start_col = start 
        end_row, end_col = end
        # extracting the height and width of the grid by looking at the grid list's dimensions
        height = len(grid)
        width = len(grid[0])

        # initializing the array of nodes with their positions
        nodes = [[Node(j, i) for i in range(width)] for j in range(height)]
        nodes[start_row][start_col].distance = 0
        nodes[start_row][start_col].visited = True

        for i in range(width * height): # we want to iterate through all 0-distance nodes to find all 1-distance nodes, then through 1s to find 2s, etc.
            #  A good upper bound for distance is width*height because there are only that many nodes total. In general, we will find the endpoint much sooner than that and break out
            for row in range(height):
                for col in range(width):
                    if grid[row][col] == True:
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
        while predecessor is not None:
            output.insert(0, predecessor.position)
            predecessor = predecessor.previous
        return output