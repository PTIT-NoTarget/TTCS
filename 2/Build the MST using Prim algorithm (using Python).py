class Edge:
    def __init__(self, fi, se, w):
        self.fi = fi
        self.se = se
        self.w = w


g = []
v = []
vH = []
ans = []
n = 0
st = 0
a = [[0] * 100 for _ in range(100)]
dH = 0


def cmp(a, b):
    if a.w == b.w:
        if a.fi == b.fi:
            return a.se < b.se
        return a.fi < b.fi
    return a.w < b.w


def init():
    global n, st
    n = int(input())
    st = int(input())

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            a[i][j] = row[j - 1]
            if i < j and a[i][j]:
                g.append(Edge(i, j, a[i][j]))

    for i in range(1, n + 1):
        if i == st:
            vH.append(i)
        else:
            v.append(i)
    g.sort(key=lambda x: (x.w, x.fi, x.se))


def Prim():
    global dH, ans
    while v:
        for i in g:
            if (i.fi in vH and i.se in v) or (i.se in vH and i.fi in v):
                if i.fi in vH:
                    vH.append(i.se)
                    v.remove(i.se)
                else:
                    vH.append(i.fi)
                    v.remove(i.fi)
                dH += i.w
                ans.append((i.fi, i.se))
                break


if __name__ == "__main__":
    input()
    init()
    Prim()
    print("dH =", dH)