n = int(input())
m = int(input())
ans = int(3e8)


def getMinV(r, h, k):
    res = r * r * h
    i = 1
    for _ in range(k - 1):
        res += i * i * i
        i += 1
    return res


def getMaxV(r, h, k):
    res = 0
    for _ in range(k):
        res += r * r * h
        r -= 1
        h -= 1
    return res


def getMinS(r, h, k):
    res = 2 * r * h
    i = 1
    for _ in range(k - 1):
        res += 2 * i * i
        i += 1
    return res


def dfs(hav, Lr, Lh, S, V):
    global ans, n, m
    if hav == m:
        if V == 0:
            ans = min(ans, S)
            return
    for r in reversed(range(Lr)):
        for h in reversed(range(Lh)):
            if r < m - hav or h < m - hav: continue
            if getMaxV(r, h, m - hav) < V: continue
            if getMinV()(r, h, m - hav) > V: continue
            if getMinS(r, h, m - hav) + S >= ans: continue
            detS = 2 * r * h
            if hav == 0:
                detS += r * r
            detV = r * r * h
            dfs(hav + 1, r, h, S + detS, V - detV)
    return


dfs(0, 100, 100, 0, n)
if ans > int(1e8):
    print(0)
else:
    print(ans)