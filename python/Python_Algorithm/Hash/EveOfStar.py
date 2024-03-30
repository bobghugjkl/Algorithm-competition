N, eps = 110, 1e-8
m = int(input())
n = int(input())
g = [list(input()) for _ in range(n)]
hash_val = []#全局变量一共26个英文字母


# 获取点和点的距离和为哈希值
def get_hash(q):
    sum = 0
    for i in range(len(q)):
        for j in range(i):
            sum += (((q[i][0] - q[j][0]) ** 2 + (q[i][1] - q[j][1]) ** 2) ** 0.5) #计算每两个点
    return sum


def get_id(q):
    val = get_hash(q)
    for i in range(len(hash_val)): #找有没有类似的
        if abs(hash_val[i] - val) <= eps:
            return chr(ord('a') + i)#出现过的话就返回第i个字母
    hash_val.append(val)#不然就加进去新的
    return chr(ord('a') + len(hash_val) - 1)#上一行id++了，这次先-1然后加a做循环


def dfs(a, b):
    g[a][b] = 0 #标记走过
    q.append((a, b))#存点
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if i >= 0 and i < n and j >= 0 and j < m and g[i][j] == '1':
                dfs(i, j)


for i in range(n):
    for j in range(m):
        if g[i][j] == '1':
            q = []
            dfs(i, j) #开始搜索
            id = get_id(q) #标记
            for x, y in q:
                g[x][y] = id #全部打上标记

for i in range(n):
    for j in range(m):
        print(g[i][j], end=" ")
    print()
