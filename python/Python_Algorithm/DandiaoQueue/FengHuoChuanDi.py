from collections import deque

n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))

f = [0] * (n + 1)
q = deque([0])

for i in range(1, n + 1):
    if q and i - q[0] >= m + 1:
        q.popleft()
    f[i] = f[q[0]] + w[i]

    while q and f[i] <= f[q[-1]]:
        q.pop()
    q.append(i)
print(min(f[n - m + 1:n + 1]))
