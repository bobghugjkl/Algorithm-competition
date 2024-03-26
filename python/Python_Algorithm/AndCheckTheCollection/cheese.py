N = 1010
p = [0 for i in range(N)]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


T = int(input())
for _ in range(T):
    n, h, r = map(int, input().split())
    q = [[0, 0, 0]]  # 0号位不用，提前置0
    for i in range(0, n + 2):
        p[i] = i
    for i in range(1, n + 1):
        x, y, z = map(int, input().split())
        q.append([x, y, z])
        if abs(z - 0) <= r:
            p[find(i)] = find(0)
        if abs(z - h) <= r:
            p[find(i)] = find(n + 1)
    for i in range(1, n + 1):
        for j in range(1, i):
            dx = q[i][0] - q[j][0]
            dy = q[i][1] - q[j][1]
            dz = q[i][2] - q[j][2]
            if dx * dx + dy * dy + dz * dz <= 4 * r * r:
                p[find(i)] = find(j)
    if find(0) == find(n + 1):
        print("Yes")
    else:
        print("No")
