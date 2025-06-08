# Minimum Spanning Tree using Kruskal's Algorithm
def kruskal_mst(V, edges):
    parent = list(range(V))

    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u

    def union(u, v):
        parent[find(u)] = find(v)

    mst_weight = 0
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst_weight += w
    return mst_weight

