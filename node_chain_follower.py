from templates import Action, Facing

class NodeChainFollower:
    def __init__(self, position, facing):
        self.node_chain = []
        self.my_row = position[0]
        self.my_col = position[1]
        self.my_facing = facing

    def set_chain(self, chain):
        self.node_chain = chain
        
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
    
    def get_position(self):
        return (self.my_row, self.my_col)
    def set_position(self, position):
        self.my_row = position[0]
        self.my_col = position[1]

    def get_facing(self):
        return self.my_facing