def read_graph_from_file(file_path):
    """
    Reads graph from a text file in format:
    vertex1 vertex2 weight
    """
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2, weight = line.strip().split()
            weight = int(weight)
            
            if v1 not in graph:
                graph[v1] = []
            if v2 not in graph:
                graph[v2] = []
                
            graph[v1].append((v2, weight))
            graph[v2].append((v1, weight))
    return graph

def kruskal_mst(graph):
    # Original kruskal implementation remains the same
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
    
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

# Example usage with text file
if __name__ == "__main__":
    graph = read_graph_from_file("graph_input.txt")
    mst = kruskal_mst(graph)
    print("Minimum Spanning Tree edges:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
