from collections import defaultdict
from typing import Set

class Graph:
    def __init__(self):
        """Initialize an empty undirected graph using adjacency list representation"""
        self.graph = defaultdict(list)

    def add_edge(self, source: int, destination: int) -> None:
        """
        Add an undirected edge between source and destination vertices
        
        Args:
            source: Starting vertex of the edge
            destination: Ending vertex of the edge
        """
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def dfs(self, vertex: int, visited: Set[int]) -> None:
        """
        Perform Depth First Search starting from given vertex
        
        Args:
            vertex: Current vertex being visited
            visited: Set of vertices already visited
        """
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def is_connected(self) -> bool:
        """
        Check if the graph is connected
        
        Returns:
            bool: True if graph is connected, False otherwise
        """
        if not self.graph:
            return True

        visited = set()
        start_vertex = next(iter(self.graph))
        self.dfs(start_vertex, visited)

        # Get all unique vertices including neighbors
        all_vertices = set()
        for vertex in self.graph:
            all_vertices.add(vertex)
            all_vertices.update(self.graph[vertex])

        return len(visited) == len(all_vertices)

def read_graph_from_file(filename: str) -> Graph:
    """
    Read graph data from input file
    
    Args:
        filename: Name of the input file
        
    Returns:
        Graph: Constructed graph object
    """
    graph = Graph()
    try:
        with open(filename, 'r') as file:
            num_edges = int(file.readline().strip())
            for _ in range(num_edges):
                source, destination = map(int, file.readline().strip().split())
                graph.add_edge(source, destination)
        return graph
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        exit(1)
    except ValueError:
        print("Error: Invalid input format in file")
        exit(1)

def main():
    """Main function to process graph connectivity"""
    input_file = 'graph_input.txt'
    graph = read_graph_from_file(input_file)
    
    result = "Connected" if graph.is_connected() else "Not Connected"
    print(f"The graph is {result}")

if __name__ == "__main__":
    main()
