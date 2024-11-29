class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Convert inputs to strings to handle different types uniformly
        u = str(u)
        v = str(v)
        
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        # Convert start vertex to string
        start = str(start)
        
        if visited is None:
            visited = set()
            
        visited.add(start)
        print(start, end=' ')
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage with different input types
g = Graph()

# Adding edges with mixed types
g.add_edge('A', 'B')    # strings
g.add_edge(1, 2)        # integers
g.add_edge('C', 3)      # mixed types
g.add_edge(2.5, 'D')    # float and string
g.add_edge(True, False) # booleans

print("DFS starting from vertex 'A':")
g.dfs('A')

print("\nDFS starting from vertex 1:")
g.dfs(1)
