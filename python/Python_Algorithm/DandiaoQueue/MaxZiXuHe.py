from collections import deque

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] += a[i - 1]
q = deque()
res = float('-inf')
for i in range(n + 1):
    if q and i - q[0] >= m - 1:
        q.popleft()
    if q:
        res = max(res, a[i] - a[q[0]])
    while q and a[i] <= a[q[-1]]:
        q.pop()
    q.append(i)
print(res)
