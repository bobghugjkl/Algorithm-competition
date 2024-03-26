n, m = map(int, input().split())
p = [i for i in range(n + 1)]


def find(x):
    while p[x] != x:
        p[x] = find(p[x])
    return p[x]


for _ in range(m):
    s = input().split()
    a, b = map(int, s[1:])
    a, b = find(a), find(b)
    if s[0] == 'M':
        if a != b:
            p[a] = b
    else:
        if a == b:
            print("Yes")
        else:
            print('No')
