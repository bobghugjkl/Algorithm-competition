N = 110
g = [[0] * N for _ in range(N)]
d = [[-1] * N for _ in range(N)]
queue = [(0, 0)]


def bfs():
    d[0][0] = 0
    hh, tt = 0, 0
    x, y = [-1, 0, 1, 0], [0, 1, 0, -1]
    while hh <= tt:
        t = queue.pop(0)
        hh += 1
        for i in range(4):
            point_x, point_y = t[0] + x[i], t[1] + y[i]
            if point_x >= 0 and point_x < N and point_y >= 0 and point_y < m and g[point_x][point_y] == 0 and d[point_x][
                point_y] == -1:
                d[point_x][point_y] = d[t[0]][t[1]] + 1
                tt += 1
                queue.append((point_x, point_y))
    return d[n - 1][m - 1]


n, m = map(int, input().split())
for i in range(n):
    g[i] = list(map(int, input().split()))
print(bfs())
