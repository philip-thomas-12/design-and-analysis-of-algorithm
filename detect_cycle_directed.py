def is_cyclic_util(v, visited, rec_stack, graph):
    visited[v] = True
    rec_stack[v] = True
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            if is_cyclic_util(neighbor, visited, rec_stack, graph):
                return True
        elif rec_stack[neighbor]:
            return True
    
    rec_stack[v] = False
    return False

def is_cyclic(graph, V):
    visited = [False] * V
    rec_stack = [False] * V
    for node in range(V):
        if not visited[node]:
            if is_cyclic_util(node, visited, rec_stack, graph):
                return True
    return False

# Example
graph = [
    [1],
    [2],
    [0],
    [4],
    []
]
print("Cycle Exists:" if is_cyclic(graph, 5) else "No Cycle")
