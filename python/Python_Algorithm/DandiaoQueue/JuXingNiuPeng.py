n, m, q = map(int, input().split())
a = [[0] * (m + 2) for _ in range(n + 2)]
f = [[0] * (m + 2) for _ in range(n + 2)]
while q:
    q -= 1
    x, y = map(int, input().split())
    a[x][y] = 1

'''
前缀和(列)
'''
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == 1:
            f[i][j] = 0
        else:
            f[i][j] = f[i - 1][j] + 1
res = 0
for i in range(1, n + 1):
    l = [0] * (m + 2)
    r = [0] * (m + 2)
    q = []
    for j in range(1, m + 1):
        while len(q) > 0 and f[i][q[-1]] >= f[i][j]:
            del q[-1]
        if len(q) == 0:
            l[j] = 1
        else:
            l[j] = q[-1] + 1
        q.append(j)
    q = []
    for j in range(m, 0, -1):
        while len(q) > 0 and f[i][q[-1]] >= f[i][j]:
            del q[-1]
        if len(q) == 0:
            l[j] = m
        else:
            l[j] = q[-1] - 1
        q.append(j)
    for j in range(1, m + 1):
        res = max(res, (r[j] - l[j] + 1) * f[i][j])
print(res)
