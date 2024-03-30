'''
当连的两个格子在同一个联通块里时我们认为他们已经成环
 ——
|  |
A--B
在A,B中连线可见AB在同一个连接块里，所以连接后可以成环


二维变一维==>x,y从0开始 -> x * n + y
'''
import sys

sys.setrecursionlimit(100000)
N = 40010
n, m = map(int, input().split())


def get(x, y):
    return x * n + y


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


p = [i for i in range(n * n)]

res = 0

for i in range(1,m+1):
    li = input().split()
    x, y = int(li[0]), int(li[1])
    x -= 1 #x,y必须为从0开始才有效，这里题目规定从1开始，所以我们-1
    y -= 1
    c = li[2]
    a = get(x, y)  # 编号
    if c == 'D':
        b = get(x + 1, y)  # 向下走
    else:
        b = get(x, y + 1)  # 向右走
    pa, pb = find(a), find(b)
    if pa == pb:
        res = i  # 第一次出现环的编号
        break
    p[pa] = pb  # 合并
if res == 0:
    print("draw")
else:
    print(res)
