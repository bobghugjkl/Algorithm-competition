n, m = map(int, input().split())
p = [i for i in range(n + 1)]


def find(x):
    while p[x] != x:
        p[x] = find(p[x])
    return p[x]


for _ in range(m):
    s = input().split()
    a, b = int(s[1]), int(s[2])
    if s[0] == 'M':
        p[find(a)] = find(b)
    else:
        if find(a) == find(b):
            print("Yes")
        else:
            print('No')
