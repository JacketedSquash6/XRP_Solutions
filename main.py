from utilities import NORTH
from navigator import Navigator
from robot_pilot import RobotPilot
import random

def main():
    dimensions = (5, 8)
    height, width = dimensions

    pilot = RobotPilot()
    navigator = Navigator()

    node_list = [(0,0), (0,1), (0,2), (1,2), (2,2), (1,2), (1,1), (2,1), (3,1), (4,1), (4,2), (4,3), (3,3)] # arbitrary list of coordinates, each orthogonally adjacent to the previous

    action_list = navigator.generate_actions(node_list, NORTH)
    print(action_list)
    pilot.do_actions(action_list)

if __name__ == "__main__":
    main()