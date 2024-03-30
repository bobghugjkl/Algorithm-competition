import sys

sys.setrecursionlimit(100000)
N = 10010
n, m = map(int, input().split())
p = [i for i in range(N)]
d = [0 for _ in range(N)]


def find(x):
    if p[x] == x or p[p[x]] == p[x]: #自身是最上面或者父节点是最上面就返回
        return p[x]
    r = find(p[x])# 找到p[x]
    d[x] += d[p[x]] #更新权值信息
    p[x] = r #压缩，直接让他指向父节点
    return r


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 1:
        a, b = find(a), find(b)
        if a != b:
            d[a] -= d[b]#差分（树状差分）
            p[a] = b #a作为b的儿子
    else:
        a = find(a)
        d[a] += b
for i in range(1, n + 1):
    if i == find(i):
        print(d[i], end=" ")
    else:
        print(d[i] + d[find(i)], end=" ") #d[p[x]] + d[x] + d[r]
print()
