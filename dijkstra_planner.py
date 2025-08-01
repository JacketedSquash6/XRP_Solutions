from utilities import Node

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

class DijkstraPlanner:
    def __init__(self, dimensions, obstacles):
        self.height = dimensions[0]
        self.width = dimensions[1]
        self.obstacles = obstacles

    def plan(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        nodes = [[Node(j, i) for i in range(self.width)] for j in range(self.height)]
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
            if row < self.height-1:
                neighbors.append(nodes[row+1][col])
            if row > 0:
                neighbors.append(nodes[row-1][col])
            if col < self.width-1:
                neighbors.append(nodes[row][col+1])
            if col > 0:
                neighbors.append(nodes[row][col-1])

            for neighbor in neighbors:
                if neighbor.visited: # already found shortest path to this node, no use looking at it again
                    continue
                if neighbor.position in self.obstacles: # if the location is blocked, don't navigate through it
                    continue
                if neighbor.distance is None or neighbor.distance > node.distance + 1:
                    neighbor.distance = node.distance + 1
                    neighbor.previous = node
                    q.put((neighbor.distance, neighbor))
        output = []
        predecessor = nodes[end_row][end_col]
        while predecessor is not None:
            output.insert(0, predecessor.position)
            predecessor = predecessor.previous
        return output    