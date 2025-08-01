from navigator import Navigator
from manhattan_planner import ManhattanPlanner
from robot_pilot import RobotPilot
import random

def main():
    dimensions = (5, 8)
    height, width = dimensions

    pilot = RobotPilot()

    planner = ManhattanPlanner(dimensions)

    navigator = Navigator(planner)

    targets = [] # This list can be written by hand. In that case, comment out the code below which randomly generates targets
    while len(targets) < 10:
        t_row = random.randint(0, height-1)
        t_col = random.randint(0, width-1)
        targets.append((t_row, t_col))

    score = 0
    for target in targets:
        print("Navigating to Target", target)
        action_list = navigator.navigate_to(pilot.get_position(), pilot.get_facing(), target)
        print(action_list)
        pilot.do_actions(action_list)
        
        if pilot.get_position() == target:
            print("Arrived at Target", target)
            score += 1
        else:
            print("Failed to arrive at Target", target)
    
    print("The Robot successfully navigated to", score, "out of", len(targets), "targets")

if __name__ == "__main__":
    main()