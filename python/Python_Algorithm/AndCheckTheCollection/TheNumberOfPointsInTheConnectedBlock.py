N = 100010
p = [0] * N
size = [0] * N


def find(x):
    while x != p[x]:
        p[x] = find(x)
    return p[x]


n, m = map(int, input().split())
for i in range(1, n + 1):
    p[i] = i
    size[i] = 1

while m:
    m -= 1
    li = input().split()
    if li[0] == 'C':
        a, b = int(li[1]), int(li[2])
        if find(a) != find(b):
            size[find(b)] += size(find(a))
            p[find(a)] = find(b)
        else:
            continue
    elif li[0] == 'Q1':
        a, b = int(li[1]), int(li[2])
        if find(a) == find(b):
            print("Yes")
        else:
            print("No")
    else:
        a = int(li[1])
        print(size[find(a)])
