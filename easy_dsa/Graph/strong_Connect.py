from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def find_scc(self):
        # Step 1: Get vertices in order of finishing time
        stack = []
        visited = set()
        
        for vertex in self.graph:
            if vertex not in visited:
                self._dfs(vertex, visited, stack)
        
        # Step 2: Create reversed graph
        reversed_graph = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph.add_edge(v, u)
        
        # Step 3: Process vertices in order from stack
        visited.clear()
        components = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                reversed_graph._collect_scc(vertex, visited, component)
                components.append(component)
        
        return components
    
    def _dfs(self, vertex, visited, stack):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(vertex)
    
    def _collect_scc(self, vertex, visited, component):
        visited.add(vertex)
        component.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._collect_scc(neighbor, visited, component)

# Example usage
def main():
    # Read from file
    g = Graph()
    with open('input.txt', 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            g.add_edge(u, v)
    
    # Find and print SCCs
    sccs = g.find_scc()
    print("Strongly Connected Components:")
    for i, scc in enumerate(sccs, 1):
        print(f"Component {i}:", scc)

if __name__ == "__main__":
    main()
