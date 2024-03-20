from collections import deque
input()
n = int(input())
a = [[0] * n for _ in range (n)]

for i in range(n):
    a[i] = list(map(int, input().split()))
    
visited = [0] * (n + 6)

def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    print(chr(x + 65), end = " ")
    while q:
        x = q.popleft()
        for i in range(n):
            if a[x][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
                print(chr(i + 65), end = " ")
                
def DFS(x):
    visited[x] = 1
    print(chr(x + 65), end = " ")
    for i in range(n):
        if a[x][i] == 1 and visited[i] == 0:
            DFS(i)
                
y = int(input())    
if y == 1:
    print("1. Test breadth-first traversal:")
elif y == 2:
    print("2. Test depth-first traversal:")

for i in range(0, n):
    if visited[i] == 0:
        if y == 1:
            BFS(i)
        else:
            DFS(i)
    