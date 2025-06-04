from templates import Node
from priority_queue import PriorityQueue

def dijkstra(map, start, end):
    start_row, start_col = start
    end_row, end_col = end
    height = len(map)
    width = len(map[0])
    nodes = [[Node(j, i) for i in range(width)] for j in range(height)]
    nodes[start_row][start_col].distance = 0
    q = PriorityQueue()
    q.put((0, nodes[start_row][start_col]))

    while nodes[end_row][end_col].distance is None and not q.empty():
        distance, node = q.get()
        row, col = node.position
        if node.visited:
            continue
        node.visited = True

        neighbors = []
        if row < height-1:
            neighbors.append(nodes[row+1][col])
        if row > 0:
            neighbors.append(nodes[row-1][col])
        if col < width-1:
            neighbors.append(nodes[row][col+1])
        if col > 0:
            neighbors.append(nodes[row][col-1])

        for neighbor in neighbors:
            if neighbor.visited: # already found shortest path to this node, no use looking at it again
                continue
            if neighbor.distance is None or neighbor.distance > node.distance + 1:
                neighbor.distance = node.distance + 1
                neighbor.previous = node
                q.put((neighbor.distance, neighbor))
    output = []
    predecessor = nodes[end_row][end_col]
    while predecessor.previous is not None:
        output.insert(0, predecessor.position)
        predecessor = predecessor.previous
    return output    