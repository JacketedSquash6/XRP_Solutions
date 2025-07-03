class Action:
    TURN_LEFT = 0
    TURN_RIGHT = 1
    FORWARD = 2
    DONE = 3 # TODO Leave this out in the initial code, so that students can come up with the fact that they need a new function

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
        
class PriorityQueue:
    def __init__(self):
        self.array = []
        
    def put(self, item):
        key = item[0]
        # else
        for i in range(len(self.array)):
            key_at_i = self.array[i][0]
            if key < key_at_i:
                self.array.insert(i, item)
                return
        # if this is the largest so far (or equal), it goes at the end
        self.array.append(item)
    def empty(self):
        return len(self.array) == 0
    def get(self):
        return self.array.pop(0)
        
def dijkstra(map, start, end):
    start_row, start_col = start
    end_row, end_col = end
    height = len(map)
    width = len(map[0])
    nodes = [[Node(j, i) for i in range(width)] for j in range(height)]
    nodes[start_row][start_col].distance = 0
    q = PriorityQueue()
    q.put((0, nodes[start_row][start_col]))

    while nodes[end_row][end_col].distance is None and not q.empty():
        distance, node = q.get()
        row, col = node.position
        if node.visited:
            continue
        node.visited = True

        neighbors = []
        if row < height-1:
            neighbors.append(nodes[row+1][col])
        if row > 0:
            neighbors.append(nodes[row-1][col])
        if col < width-1:
            neighbors.append(nodes[row][col+1])
        if col > 0:
            neighbors.append(nodes[row][col-1])

        for neighbor in neighbors:
            if neighbor.visited: # already found shortest path to this node, no use looking at it again
                continue
            if map[neighbor.position[0]][neighbor.position[1]] == True: # if the location is blocked, don't navigate through it
                continue
            if neighbor.distance is None or neighbor.distance > node.distance + 1:
                neighbor.distance = node.distance + 1
                neighbor.previous = node
                q.put((neighbor.distance, neighbor))
    output = []
    predecessor = nodes[end_row][end_col]
    while predecessor.previous is not None:
        output.insert(0, predecessor.position)
        predecessor = predecessor.previous
    return output    