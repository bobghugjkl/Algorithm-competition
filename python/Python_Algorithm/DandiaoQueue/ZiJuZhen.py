from collections import deque
from sys import stdin, stdout

input = stdin.readline

MOD = 9928244353
n, m, a, b = map(int, input().split())
mat = []
for _ in range(n):
    L = list(map(int, input().split()))
    mat.append(L)
# 记录
max_mat = [[-float("inf")] * m for _ in range(n)]
min_mat = [[float("inf")] * m for _ in range(n)]

for j in range(m):
    q1 = deque([])
    q2 = deque([])
    for i in range(a - 1):
        while len(q1) > 0 and mat[i][j] >= mat[q1[-1]][j]:
            q1.pop()
        while len(q2) > 0 and mat[i][j] <= mat[q2[-1]][j]:
            q2.pop()
        q1.append(i)
        q2.append(i)
        max_mat[i][j] = mat[q1[0]][j]
        min_mat[i][j] = mat[q2[0]][j]
    for i in range(a - 1, n):
        while len(q1) > 0 and mat[i][j] >= mat[q1[-1]][j]:
            q1.pop()
        while len(q2) > 0 and mat[i][j] <= mat[q2[-1]][j]:
            q2.pop()
        q1.append(i)
        q2.append(i)
        max_mat[i][j] = mat[q1[0]][j]
        min_mat[i][j] = mat[q2[0]][j]
        if q1[0] == i - (a - 1):
            q1.popleft()
        if q2[0] == i - (a - 1):
            q2.popleft()

for i in range(n):
    q1 = deque([])
    L1, L2 = [], []  # 存最大值最小值
    q2 = deque([])
    for j in range(b - 1):
        while len(q1) > 0 and mat[i][j] >= mat[i][q1[-1]]:
            q1.pop()
        while len(q2) > 0 and mat[i][j] <= mat[i][q2[-1]]:
            q2.pop()
        q1.append(j)
        q2.append(j)

        L1.append(max_mat[i][q1[0]])
        L2.append(min_mat[i][q2[0]])
    for j in range(b - 1, m):
        while len(q1) > 0 and mat[i][j] >= mat[i][q1[-1]]:
            q1.pop()
        while len(q2) > 0 and mat[i][j] <= mat[i][q2[-1]]:
            q2.pop()
        q1.append(j)
        q2.append(j)

        L1.append(max_mat[i][q1[0]])
        L2.append(min_mat[i][q2[0]])
        if q1[0] == j - (b - 1):
            q1.popleft()
        if q2[0] == j - (b - 1):
            q2.popleft()
    max_mat[i] = L1
    min_mat[i] = L2
ans = 0
for i in range(a - 1, n):
    for j in range(b - 1, m):
        ans = (ans + max_mat[i][j] * min_mat[i][j]) % MOD
print(ans)
