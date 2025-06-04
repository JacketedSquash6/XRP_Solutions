from templates import Action, Facing
from random_navigator import RandomNavigator
from dijkstra_perfect_navigator import DijktstraPerfectNavigator
# from naive_search_navigator import NaiveSearchNavigator
from simulator_pilot import SimulatorPilot

def main():
    map = [[False for i in range(6)] for j in range(6)]
    pilot = SimulatorPilot(map)
    navigator = DijktstraPerfectNavigator((0,0), Facing.NORTH, map)

    targets = [(4,1), (3,3), (5,5), (0, 4), (0,0)]
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