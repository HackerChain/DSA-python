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
    
    # Test case 1: Connected graph
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    print("Test case 1:", "Connected" if g.is_connected() else "Not connected")
    
    # Test case 2: Disconnected graph
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(2, 3)
    print("Test case 2:", "Connected" if g2.is_connected() else "Not connected")

if __name__ == "__main__":
    main()
