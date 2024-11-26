class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal_mst(graph):
    """
    Implementation of Kruskal's Minimum Spanning Tree Algorithm
    
    Args:
        graph: Dictionary of the format {vertex: [(neighbor, weight)]}
    
    Returns:
        List of tuples representing edges in MST: [(vertex1, vertex2, weight)]
    """
    # Edge list creation
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if (neighbor, vertex, weight) not in edges:  # Avoid duplicate edges
                edges.append((vertex, neighbor, weight))
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    vertices = list(graph.keys())
    ds = DisjointSet(vertices)
    mst = []
    
    for edge in edges:
        vertex1, vertex2, weight = edge
        
        if ds.find(vertex1) != ds.find(vertex2):
            ds.union(vertex1, vertex2)
            mst.append(edge)
    
    return mst

# Example usage:
if __name__ == "__main__":
    # Example graph represented as adjacency list with weights
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    mst = kruskal_mst(graph)
    print("Minimum Spanning Tree edges:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
