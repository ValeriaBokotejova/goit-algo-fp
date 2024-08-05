import heapq

def dijkstra(graph, start):
    # Priority queue: (distance, vertex)
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def main():

    graph = {
        'A': {'B' : 2, 'C' : 3},
        'B': {'A' : 2, 'D': 4},
        'C': {'A' : 3, 'B': 2, 'D' : 5},
        'D': {'B' : 4, 'C': 5}
    }

    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)

    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"Vertex {vertex}: {distance}")

if __name__ == "__main__":
    main()