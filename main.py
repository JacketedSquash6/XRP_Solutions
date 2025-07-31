from navigator import Navigator
from simulator_pilot import SimulatorPilot
# from robot_pilot import RobotPilot
import random
from utilities import display

def main():
    height, width = (6,6)
    grid = [[(random.random() < 0.1) for i in range(width)] for j in range(height)]
    pilot = SimulatorPilot(grid)
    # pilot = RobotPilot()

    targets = []
    while len(targets) < 10:
        t_row = random.randint(0, height-1)
        t_col = random.randint(0, width-1)
        if not grid[t_row][t_col]: # targets can't be placed at blocked intersections
            targets.append((t_row, t_col))

    display(grid, pilot.get_position(), pilot.get_facing())
    score = 0
    for target in targets:
        print("Navigating to Target", target)
        action_list = Navigator.navigate_to(grid, pilot.get_position(), pilot.get_facing(), target)
        print(action_list)
        pilot.do_actions(action_list)
        display(grid, pilot.get_position(), pilot.get_facing())
        
        if pilot.get_position() == target:
            print("Arrived at Target", target)
            score += 1
        else:
            print("Failed to arrive at Target", target)
    
    print("The Robot successfully navigated to", score, "out of", len(targets), "targets")

if __name__ == "__main__":
    main()