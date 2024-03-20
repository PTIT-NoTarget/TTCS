import heapq

def dijkstra(n, graph, start, destination):
    # Initialize distances from start node to all other nodes as infinity
    distances = [float('inf')] * n
    
    # Mark the start node distance as 0
    distances[start] = 0
    
    # Priority queue to store nodes to be visited next
    pq = [(0, start)]
    
    # Previous node for each node
    prev = [-1] * n
    
    # Dijkstra's algorithm
    while pq:
        # Pop the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # If current node is the destination, terminate the algorithm
        if current_node == destination:
            break
        
        # If the current distance is already greater than the stored distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            # If the new distance is shorter, update the distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node
                # Add the neighbor to the priority queue with updated distance
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct the shortest path from start to destination
    path = []
    node = destination
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()
    
    # Return the shortest distance and the shortest path
    return distances[destination], path

input()
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            graph[i].append((j, row[j]))

start, destination = input().split()
start = int(start)
destination = int(destination)

shortest_distance, shortest_path = dijkstra(n, graph, start, destination)
print("Dijkstra's shortest path algorithm:")
print(f"The shortest distance from vertex {start} to {destination} is {shortest_distance}")
print("The shotest path is ", end = "")
for i in range(len(shortest_path)):
    if i != len(shortest_path) - 1:
        print(shortest_path[i], end = " -> ")
    else:
        print(shortest_path[i])
