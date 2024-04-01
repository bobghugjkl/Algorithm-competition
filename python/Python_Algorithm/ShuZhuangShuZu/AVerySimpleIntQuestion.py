from sys import stdin, stdout

input = stdin.readline


def add(x, val):
    while x <= n:
        b[x] += val
        x += lowbit(x)


def querry(x):
    res = 0
    while x:
        res += b[x]
        x -= lowbit(x)
    return res


def lowbit(x):
    return x & (-x)


N = 100010
b = [0] * N
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    add(i, a[i] - a[i-1])
for _ in range(m):
    s = input().split()
    if s[0] == 'Q':
        c = int(s[1])
        print(querry(c))
    else:
        c, d, e = int(s[1]), int(s[2]), int(s[3])
        add(c, e)
        add(d + 1, e * (-1))
