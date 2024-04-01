dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
st = set()


def bfs(a, b):
    global res1, res2
    sk = []
    sk.append((a, b))
    hh, tt = 0, 0
    st.add((a, b))
    tg = s[a][b]
    f1, f2 = True, True
    while hh <= tt:
        t = sk[hh]
        hh += 1
        for i in range(8):
            x, y = t[0] + dx[i], t[1] + dy[i]
            if 0 <= x < n and 0 <= y < n and (x, y) not in st and s[x][y] == tg:
                st.add((x, y))
                tt += 1
                sk.append((x, y))
            if 0 <= x < n and 0 <= y < n and s[x][y] != tg:
                if s[x][y] > tg:
                    f1 = False
                if s[x][y] < tg:
                    f2 = False
    if f1:
        res1 += 1
    if f2:
        res2 += 1


n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
res1, res2 = 0, 0
for i in range(n):
    for j in range(n):
        if (i, j) not in st:
            bfs(i, j)
print(res1, res2)
