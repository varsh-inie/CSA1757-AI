import heapq

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def a_star(start, goal, grid):
    open_list = [Node(start, 0, heuristic(start, goal))]
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)
        for neighbor in get_neighbors(current_node.position, grid):
            if neighbor not in closed_list:
                g_cost = current_node.g_cost + 1
                h_cost = heuristic(neighbor, goal)
                heapq.heappush(open_list, Node(neighbor, g_cost, h_cost, current_node))

    return None

def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def get_neighbors(pos, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return [(pos[0] + d[0], pos[1] + d[1]) for d in directions 
            if 0 <= pos[0] + d[0] < len(grid) and 0 <= pos[1] + d[1] < len(grid[0]) and grid[pos[0] + d[0]][pos[1] + d[1]] == 0]

def main():
    n = int(input("Enter grid size (n x n): "))
    grid = [list(map(int, input(f"Row {i}: ").split())) for i in range(n)]
    start = tuple(map(int, input("Start position (x y): ").split()))  # Input as space-separated integers
    goal = tuple(map(int, input("Goal position (x y): ").split()))  # Input as space-separated integers

    path = a_star(start, goal, grid)
    print(f"Path found: {path}" if path else "No path found")

if __name__ == "__main__":
    main()


