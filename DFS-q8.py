
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def build_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for node in range(num_nodes):
        neighbors = input(f"Enter neighbors for node {node} (space-separated): ").split()
        graph[node] = [int(x) for x in neighbors] if neighbors else []

    return graph

def main():
    graph = build_graph() 
    start_node = int(input("Enter the starting node for DFS: "))  
    visited = set()  
    print("DFS Traversal Output:")
    dfs(graph, start_node, visited)

if __name__ == "__main__":
    main()
