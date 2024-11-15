from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        "Method to add an edge to the graph"
        self.graph[u].append(v)
        
    def bfs(self, start_vertex):
        "Method to perform BFS traversal"
        # Set to keep track of visited vertices
        visited = set()
        
        # Create a queue for BFS
        queue = deque()
        
        # Add the start vertex to queue and mark it visited
        queue.append(start_vertex)
        visited.add(start_vertex)
        
        while queue:
            # Dequeue a vertex from queue and print it
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, then mark it visited
            # and enqueue it
            for adjacent in self.graph[vertex]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("BFS starting from vertex 2:")
    g.bfs(2)
