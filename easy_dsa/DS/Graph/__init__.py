class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {', '.join(map(str, self.graph[node]))}")

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("Graph representation:")
g.display()

print("\nBFS starting from node 1:")
g.bfs(1)

print("\nDFS starting from node 1:")
g.dfs(1)
