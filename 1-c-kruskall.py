class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_mst(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B', 1), ('B', 'C', 4), ('A', 'C', 3), ('C', 'D', 2), ('D', 'E', 5)]
mst = kruskal_mst(vertices, edges)
print("Kruskal's MST:", mst)
