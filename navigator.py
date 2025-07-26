from templates import Action, Facing, bfs

class Navigator:
    def __init__(self, position, facing):
        self.my_row, self.my_col = position
        self.my_facing = facing
        self.action_chain = []

    def set_target(self, target):
        self.target = target
        self.node_chain = bfs(self.map, self.get_position(), target)
    
    def select_action(self):
        if len(self.node_chain) == 0:
            return Action.DONE

        (next_row, next_col) = self.node_chain[0]
        if next_row == self.my_row + 1 and next_col == self.my_col:
            self.next_facing = Facing.NORTH
        elif next_row == self.my_row and next_col == self.my_col + 1:
            self.next_facing = Facing.EAST
        elif next_row == self.my_row - 1 and next_col == self.my_col:
            self.next_facing = Facing.SOUTH
        elif next_row == self.my_row and next_col == self.my_col - 1:
            self.next_facing = Facing.WEST
        else:
            raise RuntimeError("Navigator wants to move to a non-adjacent space")
        
        if self.next_facing == self.my_facing:
            self.my_row = next_row
            self.my_col = next_col
            self.node_chain.pop(0) # pop the front of the chain because now we're there and need to know the next place to go
            return Action.FORWARD
        
        if Facing.left(self.my_facing) == self.next_facing:
            self.my_facing = self.next_facing
            return Action.TURN_LEFT
        
        self.my_facing = Facing.right(self.my_facing)
        return Action.TURN_RIGHT
    
    def get_position(self):
        return (self.my_row, self.my_col)

    def get_facing(self):
        return self.my_facing

