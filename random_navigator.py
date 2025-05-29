from templates import Action, Facing, Navigator
from random import choice

class RandomNavigator(Navigator):
    def __init__(self, position = (0,0), facing = Facing.NORTH, map = [[False for i in range(6)] for j in range(6)]):
        super().__init__(position, facing, map)

    def set_target(self, target):
        return super().set_target(target)
    
    def select_action(self):
        return choice([Action.TURN_LEFT, Action.TURN_RIGHT, Action.FORWARD, Action.DONE])