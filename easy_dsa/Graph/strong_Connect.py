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
        
        for i in range(self.V):
            if not visited[i]:
                self.dfs_first(i, visited, stack)
        
        g_transpose = self.get_transpose()
        visited = [False] * self.V
        
        while stack:
            i = stack.pop()
            if not visited[i]:
                g_transpose.dfs_second(i, visited)
                print()
                
        return all(visited)

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        # First line contains number of vertices
        V = int(file.readline().strip())
        graph = Graph(V)
        
        # Read edges
        for line in file:
            u, v = map(int, line.strip().split())
            graph.add_edge(u, v)
    
    return graph

def main():
    # Read graph from input file
    graph = read_graph_from_file('input.txt')
    
    if graph.is_strongly_connected():
        print("Graph is strongly connected")
    else:
        print("Graph is not strongly connected")

if __name__ == "__main__":
    main()
