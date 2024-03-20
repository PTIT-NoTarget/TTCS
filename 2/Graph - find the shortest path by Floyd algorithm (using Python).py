def floyd_shortest_path(n, a, c, d):
    # Initialize the shortest distances matrix with the given graph
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                dist[i][j] = a[i][j]
    
    # Initialize the path matrix to store the previous node for each shortest path
    nextt = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                nextt[i][j] = j
    
    # Floyd's algorithm for finding shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nextt[i][j] = nextt[i][k]
    
    # Reconstruct the shortest path from start to destination
    shortest_path = []
    node = c
    while node != d:
        shortest_path.append(node)
        node = nextt[node][d]
    shortest_path.append(d)
    
    # Return the shortest distance and the shortest path
    return dist[c][d], shortest_path


input()
n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start, destination = input().split()
start = int(start)
destination = int(destination)

shortest_distance, shortest_path = floyd_shortest_path(n, graph, start, destination)
print("Floyd's shortest path algorithm:")
print(f"The shortest distance from vertex {start} to {destination} is {shortest_distance}")
print("The shotest path is ", end = "")
for i in range(len(shortest_path)):
    if i != len(shortest_path) - 1:
        print(shortest_path[i], end = " -> ")
    else:
        print(shortest_path[i])