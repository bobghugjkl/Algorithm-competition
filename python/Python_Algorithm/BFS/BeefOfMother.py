a, b, c = map(int, input().split())
N = 22
q = [[0 for i in range(3)] for j in range(N * N * N)] # 方案数
st = [[[0 for i in range(N)] for j in range(N)] for i in range(N)]


def bfs():
    hh, tt = 0, 0
    q[0] = [0, 0, c]
    st[0][0][c] = 1
    W = [a, b, c]
    while hh <= tt:
        tmp = q[hh]
        hh += 1
        for i in range(3):
            for j in range(3):
                if i != j:
                    w = tmp[:]
                    cur = min(w[i], W[j] - w[j])
                    w[i] -= cur
                    w[j] += cur
                    if st[w[0]][w[1]][w[2]] == 0:
                        st[w[0]][w[1]][w[2]] = 1
                        tt += 1
                        q[tt] = [w[0], w[1], w[2]]


bfs()
for i in range(c + 1):
    for j in range(b + 1):
        if st[0][j][i] == True:
            print(i, end=" ")
