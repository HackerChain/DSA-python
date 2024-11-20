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
        if not self.graph:
            return True

        visited = set()
        # Start DFS from the first vertex in the graph
        start_vertex = next(iter(self.graph))
        self.dfs(start_vertex, visited)

        # Check if all vertices are visited
        return len(visited) == len(self.graph)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    
    if g.is_connected():
        print("The graph is connected.")
    else:
        print("The graph is not connected.")
