import heapq

def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            # Split line into source, destination, and weight
            source, dest, weight = line.strip().split()
            weight = int(weight)
            
            # Initialize the source vertex dict if not exists
            if source not in graph:
                graph[source] = {}
            # Initialize the destination vertex dict if not exists    
            if dest not in graph:
                graph[dest] = {}
                
            # Add edges (assuming undirected graph)
            graph[source][dest] = weight
            graph[dest][source] = weight
            
    return graph

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    input_file = "graph.txt"
    graph = read_graph_from_file(input_file)
    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)
    print(f"Distances from {start_vertex}: {distances}")
