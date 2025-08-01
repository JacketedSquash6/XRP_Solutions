class ManhattanPlanner:
    def __init__(self, dimensions):
        self.height = dimensions[0]
        self.width = dimensions[1]

    def plan(self, start, end):
        # unrolling position tuples
        current_row, current_col = start 
        end_row, end_col = end

        position_list = [start]

        # going to the right row
        if current_row < end_row:
            row_increment = 1
        else:
            row_increment = -1

        while current_row != end_row:
            current_row += row_increment
            position_list.append((current_row, current_col))

        # going to the right column
        if current_col < end_col:
            col_increment = 1
        else:
            col_increment = -1

        while current_col != end_col:
            current_col += col_increment
            position_list.append((current_row, current_col))

        return position_list

