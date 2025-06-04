from templates import Navigator
from node_chain_follower import NodeChainFollower
from algorithms import dijkstra

class DijktstraPerfectNavigator(Navigator):
    def __init__(self, position, facing, map):
        self.map = map
        self.node_chain_follower = NodeChainFollower([], position, facing)

    def set_target(self, target):
        self.node_chain_follower.set_chain(dijkstra(self.map, self.node_chain_follower.get_position(), target))
    
    def select_action(self):
        return self.node_chain_follower.select_action()
    
    def receive_response(self, response):
        if response == False:
            raise Exception("Navigation Failed!")