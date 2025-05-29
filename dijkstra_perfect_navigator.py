from templates import Action, Facing, Navigator, Node
# from queue import PriorityQueue

class PriorityQueue:
    def __init__(self):
        self.array = []
    def put(self, item):
        (key, _value) = item
        # else
        for i in range(len(self.array)):
            (key_at_i, _val_at_i) = self.array[i]
            if key < key_at_i:
                self.array.insert(i, item)
                return
        # if this is the largest so far (or equal), it goes at the end
        self.array.append(item)
    def empty(self):
        return len(self.array) == 0
    def get(self):
        return self.array.pop()

class DijktstraPerfectNavigator(Navigator):
    def __init__(self, position = (0,0), facing = Facing.NORTH, map = [[False for i in range(6)] for j in range(6)]):
        super().__init__(position, facing, map)

    def set_target(self, target):
        super().set_target(target)
        self.node_chain = self.compute_node_chain()
    
    def select_action(self):
        if len(self.node_chain) == 0:
            return Action.DONE

        (next_row, next_col) = self.node_chain[0]
        if next_row == self.my_row + 1 and next_col == self.my_col:
            next_facing = Facing.NORTH
        elif next_row == self.my_row and next_col == self.my_col + 1:
            next_facing = Facing.EAST
        elif next_row == self.my_row - 1 and next_col == self.my_col:
            next_facing = Facing.SOUTH
        elif next_row == self.my_row and next_col == self.my_col - 1:
            next_facing = Facing.WEST
        else:
            raise RuntimeError("Navigator wants to move to a non-adjacent space")
        
        if next_facing == self.my_facing:
            (self.my_row, self.my_col) = self.node_chain.pop(0) # We are moving into the next node, so the next time this function is called, it will need the next next node
            return Action.FORWARD
        
        if Facing.left(self.my_facing) == next_facing:
            self.my_facing = next_facing
            return Action.TURN_LEFT
        
        self.my_facing = Facing.right(self.my_facing)
        return Action.TURN_RIGHT

    
    # Helper Functions
    def compute_node_chain(self):
        height = len(self.map)
        width = len(self.map[0])
        nodes = [[Node(j, i) for i in range(width)] for j in range(height)]
        nodes[self.my_row][self.my_col].distance = 0
        q = PriorityQueue()
        q.put((0, nodes[self.my_row][self.my_col]))

        while nodes[self.target_row][self.target_col].distance is None and not q.empty():
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

            for n in neighbors:
                if n.visited: 
                    continue
                if n.distance is None or n.distance > node.distance + 1:
                    n.distance = node.distance + 1
                    n.previous = node.position
                    q.put((n.distance, n))
        output = []
        predecessor = (self.target_row, self.target_col)
        while nodes[predecessor[0]][predecessor[1]].previous is not None:
            output.insert(0, predecessor)
            predecessor = nodes[predecessor[0]][predecessor[1]].previous
        return output    