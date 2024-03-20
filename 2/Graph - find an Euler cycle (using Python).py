def find_one_euler_cycle(n, start, graph):
    def dfs(v):
        for i in range(n):
            if graph[v][i] > 0:
                graph[v][i] -= 1
                graph[i][v] -= 1
                dfs(i)
        cycle.append(v)
    cycle = []
    dfs(start)
    print("Euler's cycle:")
    for i in range(len(cycle) - 1):
        if(i == len(cycle) - 2):
            print(chr(cycle[i] + 65), "->", chr(cycle[i + 1] + 65))
        else:
            print(chr(cycle[i] + 65), "->", end=" ")
    print()

input()
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start = int(input())
find_one_euler_cycle(n, start, graph)

