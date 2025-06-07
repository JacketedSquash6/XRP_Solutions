from templates import Navigator, Action, Facing
from node_chain_follower import NodeChainFollower
from algorithms import dijkstra

class DijktstraImperfectNavigator(Navigator):
    def __init__(self, position, facing, dimensions):
        height, width = dimensions
        self.map = [[False for i in range(width)] for j in range(height)]
        self.node_chain_follower = NodeChainFollower(position, facing)

    def set_target(self, target):
        self.target = target
        self.node_chain_follower.set_chain(dijkstra(self.map, self.node_chain_follower.get_position(), target))
    
    def select_action(self):
        self.previous_position = self.node_chain_follower.get_position()
        return self.node_chain_follower.select_action()
    
    def receive_response(self, response):
        if response == False:
            # It is only possible to fail on a forward move. self.previous_position stores the robot's true position
            # The space the NCF thought it moved into was actually blocked.
            ncf_row, ncf_col = self.node_chain_follower.get_position()
            self.map[ncf_row][ncf_col] = True
            # reset ncf to true position
            self.node_chain_follower.set_position(self.previous_position)
            # set new path accounting for blockage
            self.set_target(self.target)