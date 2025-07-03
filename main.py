from templates import Action, Facing
from navigator import Navigator
from simulator_pilot import SimulatorPilot
import random

def main():
    height, width = (6,6)
    map = [[(random.random() < 0.1) for i in range(width)] for j in range(height)]
    pilot = SimulatorPilot(map)
    navigator = Navigator((0,0), Facing.NORTH, (height, width))

    targets = []
    while len(targets) < 10:
        t_row = random.randint(0, height-1)
        t_col = random.randint(0, width-1)
        if not map[t_row][t_col]:
            targets.append((t_row, t_col))

    pilot.display()
    score = 0
    for t in targets:
        navigator.set_target(t)
        action = None
        for i in range(100): # navigator gets 100 moves to get us to target
            action = navigator.select_action()
            if action == Action.DONE:
                break
            response = take_action(pilot, action) # for the incomplete-information agents, failing movements will tell them information about the shape of the maze
            navigator.receive_response(response)
            pilot.display()
        
        if pilot.test_target(t):
            print("Arrived at Target", t)
            score += 1
        else:
            print("Failed to arrive at Target", t)
    
    print("The Robot successfully navigated to", score, "out of", len(targets), "targets")


        
def take_action(pilot, action):
    if action == Action.TURN_LEFT:
        return pilot.turn_left()
    if action == Action.TURN_RIGHT:
        return pilot.turn_right()
    if action == Action.FORWARD:
        return pilot.forward()
    else:
        return True


if __name__ == "__main__":
    main()