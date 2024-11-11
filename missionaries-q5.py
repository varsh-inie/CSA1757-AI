from collections import deque

def is_valid_state(M_L, C_L, M_R, C_R):
    return 0 <= M_L <= 3 and 0 <= C_L <= 3 and (M_L >= C_L or M_L == 0) and (M_R >= C_R or M_R == 0)

def bfs(M, C):
    start = (M, C, 1, 0, 0)  # Start state: M missionaries, C cannibals, boat on left
    goal = (0, 0, 0, M, C)    # Goal state: all on the right
    queue = deque([(start, [])])
    visited = set([start])
    
    moves = [(-1, 0, -1), (0, -1, -1), (-2, 0, -1), (0, -2, -1), (-1, -1, -1), 
             (1, 0, 1), (0, 1, 1), (2, 0, 1), (0, 2, 1), (1, 1, 1)]
    
    while queue:
        (M_L, C_L, B_L, M_R, C_R), path = queue.popleft()
        if (M_L, C_L, B_L, M_R, C_R) == goal:
            return path
        for dM_L, dC_L, dB_L in moves:
            new_M_L, new_C_L, new_B_L = M_L + dM_L, C_L + dC_L, 1 - B_L
            new_M_R, new_C_R = M_R - dM_L, C_R - dC_L
            new_state = (new_M_L, new_C_L, new_B_L, new_M_R, new_C_R)
            if is_valid_state(new_M_L, new_C_L, new_M_R, new_C_R) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
    return None

M, C = map(int, input("Enter number of missionaries and cannibals: ").split())
solution = bfs(M, C)
if solution:
    print("Solution steps:", *solution, sep='\n')
else:
    print("No solution found")
