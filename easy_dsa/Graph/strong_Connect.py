class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def get_transpose(self):
        g_transpose = Graph(self.V)
        
        for i in range(self.V):
            for j in self.graph[i]:
                g_transpose.add_edge(j, i)
        return g_transpose
    
    def dfs_first(self, v, visited, stack):
        visited[v] = True
        
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_first(i, visited, stack)
        
        stack.append(v)
        
    def dfs_second(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_second(i, visited)
    
    def is_strongly_connected(self):
        stack = []
        visited = [False] * self.V
        
        # First DFS to fill the stack
        for i in range(self.V):
            if not visited[i]:
                self.dfs_first(i, visited, stack)
        
        # Get transpose of the graph
        g_transpose = self.get_transpose()
        
        # Reset visited array
        visited = [False] * self.V
        
        # Process vertices in stack order
        while stack:
            i = stack.pop()
            if not visited[i]:
                g_transpose.dfs_second(i, visited)
                print()
                
        # Check if all vertices were visited in second DFS
        return all(visited)

# Example usage
def main():
    # Create a graph with 5 vertices
    g = Graph(5)
    
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 2)
    
    if g.is_strongly_connected():
        print("Graph is strongly connected")
    else:
        print("Graph is not strongly connected")

if __name__ == "__main__":
    main()
