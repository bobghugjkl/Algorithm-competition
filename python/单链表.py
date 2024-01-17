N = 100010
head = -1
e = [0 for i in range N]
ne = [0 for i in range N]
idx = 0

def insert_head(x):
    global idx,head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx+=1
def insert(k,x):
    global idx
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx
    idx+=1
def remove(k):
    ne[k] = ne[ne[k]]
n = int(input())
while n:
    li = input().split()
    if li[0] == 'H':
        x = int(li[1])
        insert_head(li[1])
    elif li[0] == 'I':
        k,x = int(li[1]),int(li[2])
        insert(k,x)
    else:
        if li[1]=='0':
            head = ne[head]
        k = int(li[1])
        remove(k-1)
    n-=1
i = head
res=[]
while i!=-1:
    res.append(e[i])
    i = ne[i]
print(" ".join(map(str,res)))
