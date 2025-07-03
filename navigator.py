from templates import Action, Facing
from algorithms import dijkstra

class Navigator:
    def __init__(self, position, facing, dimensions):
        self.my_row, self.my_col = position
        self.my_facing = facing
        height, width = dimensions
        self.map = [[False for i in range(width)] for j in range(height)]
        self.node_chain = []

    def set_target(self, target):
        self.target = target
        self.node_chain = dijkstra(self.map, self.get_position(), target)
    
    def select_action(self):
        if len(self.node_chain) == 0:
            return Action.DONE

        (self.next_row, self.next_col) = self.node_chain[0]
        if self.next_row == self.my_row + 1 and self.next_col == self.my_col:
            self.next_facing = Facing.NORTH
        elif self.next_row == self.my_row and self.next_col == self.my_col + 1:
            self.next_facing = Facing.EAST
        elif self.next_row == self.my_row - 1 and self.next_col == self.my_col:
            self.next_facing = Facing.SOUTH
        elif self.next_row == self.my_row and self.next_col == self.my_col - 1:
            self.next_facing = Facing.WEST
        else:
            raise RuntimeError("Navigator wants to move to a non-adjacent space")
        
        self.moving = False
        if self.next_facing == self.my_facing:
            self.node_chain.pop(0) # it's ok to pop here because if the move fails, you have to rebuild the node chain anyway
            self.moving = True
            return Action.FORWARD
        
        if Facing.left(self.my_facing) == self.next_facing:
            self.my_facing = self.next_facing
            return Action.TURN_LEFT
        
        self.my_facing = Facing.right(self.my_facing)
        return Action.TURN_RIGHT
    
    def receive_response(self, response):
        if response == True:
            if self.moving == True:
                self.my_row = self.next_row
                self.my_col = self.next_col
        else:
            self.map[self.next_row][self.next_col] = True
            self.set_target(self.target)
    
    def get_position(self):
        return (self.my_row, self.my_col)

    def get_facing(self):
        return self.my_facing

