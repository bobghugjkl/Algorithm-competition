from sys import stdin, stdout

input = stdin.readline

n = int(input())


def lowbit(x):
    return x & (-x)


def update(x, val):
    while x <= 32010:
        BIT_L[x] += val
        x += lowbit(x)


def query_pre(x):
    res = 0
    while x > 0:
        res += BIT_L[x]
        x -= lowbit(x)
    return res


count_L = [0] * n
BIT_L = [0] * 32010
for _ in range(n):
    x, y = map(int, input().split())
    count = query_pre(x + 1)
    count_L[count] += 1
    update(x + 1, 1)

for count in count_L:
    print(count)
