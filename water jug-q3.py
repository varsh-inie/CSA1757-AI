from collections import deque


def water_jug_solver(jug1_capacity, jug2_capacity, target):
    
    queue = deque([(0, 0)])
    visited = set()  
    visited.add((0, 0)) 

    
    while queue:
        jug1, jug2 = queue.popleft()

       
        if jug1 == target or jug2 == target:
            print(f"Solution found: Jug1={jug1} Jug2={jug2}")
            return True

      
        next_states = [
            (jug1_capacity, jug2),            
            (jug1, jug2_capacity),          
            (0, jug2),                         
            (jug1, 0),                         
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   
        ]

       
        for state in next_states:
          
            if state not in visited:
                visited.add(state)
                queue.append(state)

   
    print("No solution found.")
    return False


jug1_capacity = 4  
jug2_capacity = 3  
target = 2         


water_jug_solver(jug1_capacity, jug2_capacity, target)
