from utilities import NORTH, EAST, SOUTH, WEST, facing_left, facing_right, facing_opposite, TURN_LEFT, TURN_RIGHT, FORWARD

class Navigator:
    def __init__(self, planner):
        self.planner = planner

    def navigate_to(self, position, facing, target):
        node_list = self.planner.plan(position, target)
        action_list = Navigator.generate_actions(node_list, facing)
        return action_list

    def generate_actions(node_list, initial_facing):
        action_list = [] # This is what we will return
        current_row = node_list[0][0] # Our initial position is the first item in the node chain
        current_col = node_list[0][1]
        node_list.pop(0) # remove initial position so we can navigate to the next position
        current_facing = initial_facing # Our initial facing is given

        while len(node_list) > 0:
            next_row = node_list[0][0] # At any given moment, the next position we have to navigate to will be at the front of the list
            next_col = node_list[0][1]

            # Based on where we're going, decide which way we need to face
            if next_row == current_row + 1 and next_col == current_col: 
                next_facing = NORTH
            elif next_row == current_row and next_col == current_col + 1:
                next_facing = EAST
            elif next_row == current_row - 1 and next_col == current_col:
                next_facing = SOUTH
            elif next_row == current_row and next_col == current_col - 1:
                next_facing = WEST
            else:
                raise RuntimeError("Navigator wants to move to a non-adjacent space")
            
            # Based on which way we have to face to get where we're going, add different instructions to the list
            if next_facing == current_facing:
                action_list.append(FORWARD)
            elif next_facing == facing_left(current_facing):
                action_list.append(TURN_LEFT)
                action_list.append(FORWARD)
            elif next_facing == facing_right(current_facing):
                action_list.append(TURN_RIGHT)
                action_list.append(FORWARD)
            elif next_facing == facing_opposite(current_facing):
                # action_list.append(TURN_AROUND) # If there is a turn_around function, it is equally appropriate to call it instead of two 90degree turns
                action_list.append(TURN_LEFT)
                action_list.append(TURN_LEFT)
                action_list.append(FORWARD)
            else:
                raise RuntimeError("Navigator has invalid facing")
            
            # After executing the queued instructions, the robot will be at a new position and facing. We update this for future computations
            current_facing = next_facing
            current_row = next_row
            current_col = next_col
            node_list.pop(0)
        
        return action_list
    
    def collision(self, position, facing):
        row = position[0]
        col = position[1]

        # calculate the location of the obstacle you ran into
        if facing == NORTH:
            obstacle = (row + 1, col)
        elif facing == EAST:
            obstacle = (row, col + 1)
        elif facing == SOUTH:
            obstacle = (row - 1, col)
        elif facing == WEST:
            obstacle = (row, col - 1)

        self.planner.obstacles.append(obstacle)