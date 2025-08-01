from navigator import Navigator
# from manhattan_planner import ManhattanPlanner
from bfs_planner import BFSPlanner
from simulator_pilot import SimulatorPilot
# from robot_pilot import RobotPilot
import random
from utilities import display

def main():
    dimensions = (5, 8)
    height, width = dimensions

    pilot = SimulatorPilot(dimensions)
    obstacles = pilot.get_obstacles_list() # If using a SimulatorPilot, it will generate obstacles randomly and can supply a list of them
    # pilot = RobotPilot()
    # obstacles = [(1,1), (3,2), (4,5)] # If using a RobotPilot, this list should contain the real locations of the obstacles.

    # planner = ManhattanPlanner(dimensions)
    planner = BFSPlanner(dimensions, obstacles)

    navigator = Navigator(planner)

    targets = [] # This list can be written by hand. In that case, comment out the code below which randomly generates targets
    while len(targets) < 10:
        t_row = random.randint(0, height-1)
        t_col = random.randint(0, width-1)
        if (t_row, t_col) not in obstacles: # targets can't be placed at blocked intersections
            targets.append((t_row, t_col))

    display(dimensions, obstacles, pilot.get_position(), pilot.get_facing())
    score = 0
    for target in targets:
        print("Navigating to Target", target)
        action_list = navigator.navigate_to(pilot.get_position(), pilot.get_facing(), target)
        print(action_list)
        pilot.do_actions(action_list)
        display(dimensions, obstacles, pilot.get_position(), pilot.get_facing())
        
        if pilot.get_position() == target:
            print("Arrived at Target", target)
            score += 1
        else:
            print("Failed to arrive at Target", target)
    
    print("The Robot successfully navigated to", score, "out of", len(targets), "targets")

if __name__ == "__main__":
    main()