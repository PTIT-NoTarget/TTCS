class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def cmp(a, b):
    if a.w != b.w:
        return a.w < b.w
    if a.u != b.u:
        return a.u < b.u
    return a.v < b.v


n, dH = 0, 0
a = [[0] * 105 for _ in range(105)]
edges = []
parent = list(range(105))


def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def join(u, v):
    u = find(u)
    v = find(v)
    if v == u:
        return
    parent[v] = u


def kruskal():
    ans = []
    global dH
    for i in edges:
        if len(ans) == n - 1:
            break
        if find(i.u) != find(i.v):
            join(i.u, i.v)
            dH += i.w
            ans.append((i.u, i.v))
    print("dH =", dH)
    for i in ans:
        print(i[0], i[1])


def init():
    global n
    n = int(input())
    for i in range(1, n + 1):
        parent[i] = i

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            a[i][j] = row[j - 1]
            if a[i][j] and i < j:
                edges.append(Edge(i, j, a[i][j]))
    edges.sort(key=lambda x: (x.w, x.u, x.v))


if __name__ == "__main__":
    input()
    init()
    kruskal()