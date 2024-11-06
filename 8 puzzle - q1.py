import heapq


GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  
]


MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def find_empty_tile(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j
    return None

def calculate_manhattan_distance(state):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance


def move_tile(state, empty_tile, direction):
    row, col = empty_tile
    delta_row, delta_col = MOVES[direction]
    new_row, new_col = row + delta_row, col + delta_col
    if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
        
        new_state = [list(row) for row in state]
        new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
        return new_state
    return None


def is_goal(state):
    return state == GOAL_STATE


def a_star_search(start_state):
   
    open_list = []
    heapq.heappush(open_list, (0, start_state, [])) 
    visited = set()

    while open_list:
       
        _, current_state, path = heapq.heappop(open_list)
        visited.add(tuple(map(tuple, current_state)))  

        
        if is_goal(current_state):
            return current_state  

      
        empty_tile = find_empty_tile(current_state)

        
        for direction in MOVES:
            new_state = move_tile(current_state, empty_tile, direction)
            if new_state and tuple(map(tuple, new_state)) not in visited:
                
                cost = len(path) + 1 + calculate_manhattan_distance(new_state) 
                heapq.heappush(open_list, (cost, new_state, path + [direction]))

    return None  


def solve_8_puzzle(start_state):
    solution_state = a_star_search(start_state)
    if solution_state:
        print("Solution found! Final solved puzzle state:")
        for row in solution_state:
            print(row)
    else:
        print("No solution exists for this puzzle.")

# Example usage
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solve_8_puzzle(start_state)
