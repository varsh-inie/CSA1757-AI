from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex])
    
    return visited

# User input for graph
graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))
for i in range(num_nodes):
    node = int(input(f"Enter node {i + 1}: "))
    neighbors = list(map(int, input(f"Enter neighbors of node {node} (space-separated): ").split()))
    graph[node] = neighbors

start_node = int(input("Enter the starting node for BFS: "))
print("BFS Traversal:", bfs(graph, start_node))
