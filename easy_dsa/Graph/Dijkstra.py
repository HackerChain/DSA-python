#!/usr/bin/env python3

import heapq
from typing import Dict, List, Tuple
import sys

class Graph:
    def __init__(self):
        self.vertices: Dict[str, Dict[str, int]] = {}
    
    def add_edge(self, source: str, destination: str, weight: int) -> None:
        """Add an edge to the graph with given weight."""
        # Initialize vertices if they don't exist
        if source not in self.vertices:
            self.vertices[source] = {}
        if destination not in self.vertices:
            self.vertices[destination] = {}
        
        # Add bidirectional edges
        self.vertices[source][destination] = weight
        self.vertices[destination][source] = weight
    
    def get_vertices(self) -> List[str]:
        """Return list of all vertices in the graph."""
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex: str) -> Dict[str, int]:
        """Return all neighbors of a vertex with their weights."""
        return self.vertices.get(vertex, {})

def read_graph_from_file(filename: str) -> Graph:
    """
    Read graph from a text file and return a Graph object.
    
    File format:
    source_vertex destination_vertex weight
    Example:
    A B 5
    B C 3
    """
    graph = Graph()
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    # Skip empty lines and comments
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse the line
                    parts = line.split()
                    if len(parts) != 3:
                        raise ValueError(f"Invalid format at line {line_number}")
                    
                    source, dest, weight = parts
                    weight = int(weight)
                    
                    if weight < 0:
                        raise ValueError(f"Negative weight at line {line_number}")
                    
                    graph.add_edge(source, dest, weight)
                    
                except ValueError as e:
                    print(f"Error in line {line_number}: {e}")
                    sys.exit(1)
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
        
    return graph

def dijkstra(graph: Graph, start: str) -> Dict[str, float]:
    """
    Implementation of Dijkstra's shortest path algorithm.
    Returns dictionary of shortest distances from start vertex to all others.
    """
    if start not in graph.get_vertices():
        raise ValueError(f"Start vertex '{start}' not found in graph")
    
    # Initialize distances and priority queue
    distances: Dict[str, float] = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    priority_queue: List[Tuple[float, str]] = [(0, start)]
    visited: Dict[str, bool] = {vertex: False for vertex in graph.get_vertices()}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if we've found a better path already
        if visited[current_vertex]:
            continue
            
        visited[current_vertex] = True
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_vertex).items():
            if visited[neighbor]:
                continue
                
            distance = current_distance + weight
            
            # Update distance if we found a better path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    """Main function to run the program."""
    if len(sys.argv) != 2:
        print("Usage: python dijkstra_enhanced.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    start_vertex = 'A'  # Can be modified or taken as command line argument
    
    try:
        # Read graph and compute shortest paths
        graph = read_graph_from_file(input_file)
        distances = dijkstra(graph, start_vertex)
        
        # Print results
        print("\nShortest distances from vertex", start_vertex)
        print("-" * 40)
        for vertex, distance in sorted(distances.items()):
            print(f"To {vertex}: {distance if distance != float('infinity') else 'unreachable'}")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
