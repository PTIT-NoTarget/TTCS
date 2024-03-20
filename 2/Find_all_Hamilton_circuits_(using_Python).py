def find_all_hamilton_circuits(n, start, graph):
    def is_valid(v, pos, path):
        if graph[path[pos-1]][v] == 0:
            return False
        if v in path:
            return False
        return True
    def hamilton_circuit(path, pos):
        if pos == n:
            if graph[path[pos-1]][path[0]] == 1:
                print(*[i+1 for i in path], path[0]+1)
            return
        for v in range(n):
            if is_valid(v, pos, path):
                path[pos] = v
                hamilton_circuit(path, pos+1)
                path[pos] = -1
    path = [-1] * n
    path[0] = start
    hamilton_circuit(path, 1)

input()
n = int(input()) 
start = int(input()) - 1
graph = [list(map(int, input().split())) for _ in range(n)]
find_all_hamilton_circuits(n, start, graph)