N = 100010
e = [0]*N
l = [0]*N
r = [0]*N
r[0] = 1
l[1] = 0
idx = 2

# 在第k个点的右侧插入x
def insert(k,x):
    global idx
    e[idx] = x
    r[idx] = r[k]
    l[idx] = k
    l[r[k]] = idx
    r[k] = idx
    idx += 1

# 删除第k个结点数
def remove(k):
    r[l[k]] = r[k]
    l[r[k]] = l[k]

n = int(input())
while n:
    li = input().split()
    if li[0] == 'L':
        insert(0,int(li[1]))
    elif li[0] == 'R':
        insert(l[1],int(li[1]))
    elif li[0] == 'D':
        remove(int(li[1])+1)
    elif li[0] == 'IL':
        insert(l[int(li[1])+1],int(li[2]))
    else:
        insert(int(li[1])+1,int(li[2]))
    n -= 1
i = r[0]
res = []
while i != 1:
    res.append(str(e[i]))
    i = r[i]
print(" ".join(res))

