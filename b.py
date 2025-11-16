from collections import deque

def bfs_directed(graph, start_node, goal_node):
    if start_node == goal_node:
        return [start_node]
    
    queue = deque([start_node])
    visited = {start_node}
    parent_map = {start_node: None}
    
    print(f"Starting BFS from {start_node} to {goal_node} on DIRECTED graph...")
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = current_node
                
                if neighbor == goal_node:
                    path = []
                    node = goal_node
                    while node is not None:
                        path.append(node)
                        node = parent_map.get(node)
                    return path[::-1]  
                
                queue.append(neighbor)
    
    return "Goal node not reachable"

GRAPH_DIRECTED = {
    1: [2, 4],
    2: [],
    3: [2, 5],
    4: [3, 6],
    5: [7],
    6: [8],
    7: [8],
    8: []
}

start_node = 1
goal_node = 8

if __name__ == "__main__":
    shortest_path = bfs_directed(GRAPH_DIRECTED, start_node, goal_node)
    print("Shortest Path:")
    print(shortest_path)
