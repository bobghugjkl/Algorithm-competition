import sys

input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(x, y):
    global res
    total, bound = 0, 0
    q = [[x, y]]
    st[x][y] = True
    while q:
        x, y = q.pop(0)
        total += 1
        is_bound = False
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if a < 0 or a >= n or b < 0 or b >= n:
                continue
            if g[a][b] == '.':
                is_bound = True
                continue
            if g[a][b] == '#' and not st[a][b]:
                q.append([a, b])
                st[a][b] = True
        if is_bound == True:
            bound += 1
    if total == bound:
        res += 1


n = int(input())
g = [0] * n
st = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    g[i] = list(input())
res = 0
for i in range(n):
    for j in range(n):
        if not st[i][j] and g[i][j] == "#":
            bfs(i, j)
print(res)
