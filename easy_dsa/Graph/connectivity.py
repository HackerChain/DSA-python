from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def dfs(self, v, visited):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    def is_connected(self):
        # Empty graph is considered connected
        if not self.graph:
            return True
        
        visited = set()
        start_vertex = next(iter(self.graph))
        self.dfs(start_vertex, visited)
        
        # Check if all vertices are reachable
        all_vertices = set()
        for vertex in self.graph:
            all_vertices.add(vertex)
            all_vertices.update(self.graph[vertex])
            
        return len(visited) == len(all_vertices)

def main():
    g = Graph()
    
    # Reading from input file
    with open('graph_input.txt', 'r') as file:
        num_edges = int(file.readline().strip())
        for _ in range(num_edges):
            u, v = map(int, file.readline().strip().split())
            g.add_edge(u, v)
    
    # Check and print connectivity
    print("Graph is", "Connected" if g.is_connected() else "Not connected")

if __name__ == "__main__":
    main()
