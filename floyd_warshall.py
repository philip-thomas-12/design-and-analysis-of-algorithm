# All-pairs shortest path using Floyd-Warshall Algorithm
def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

