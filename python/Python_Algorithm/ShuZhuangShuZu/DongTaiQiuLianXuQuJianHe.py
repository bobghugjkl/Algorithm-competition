def low_bit(x):
    return x & (-1)


def querry(x):
    res = 0
    while x:
        res += b[x]
        x -= low_bit(x)
    return res


def add(x, val):
    while x < 100010:
        b[x] += val
        x += low_bit(x)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * int(100010)
for i in range(len(a)):
    add(i + 1, a[i])
for _ in range(m):
    d, e, f = map(int, input().split())
    if d == 0:
        count = querry(f) - querry(e - 1)
        print(count)
    else:
        add(e, f)
