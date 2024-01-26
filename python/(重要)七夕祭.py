def work(n, a):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
    if cnt % n:
        return -1
    avg = cnt // n
    c = [0] * (n)
    for i in range(1, n):
        c[i] = s[i] - (i) * avg
    c.sort()
    res = 0
    for i in range(n):
        res += abs(c[i] - c[n // 2])
    return res

n, m, cnt = map(int, input().split())
row = [0] * (n + 1)
col = [0] * (m + 1)
for _ in range(cnt):
    x, y = map(int, input().split())
    row[x] += 1
    col[y] += 1

r = work(n, row)
c = work(m, col)
if r!=-1 and c!=-1:
    print("both",r+c)
elif r!=-1:
    print("row",r)
elif c!=-1:
    print("column",c)
else:
    print("impossible")
