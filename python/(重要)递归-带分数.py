n = int(input())
st = [False for i in range(10)]
backup = [False for i in range(10)]
ans = 0
def check(a,c):
    global n
    b = n*c-a*c
    if b<=0 or a<=0 or c<=0:
        return False
    backup = st[:]
    while b:
        x = b % 10
        b //= 10
        if (not x)or(backup[x]):
            return False
        backup[x] = True
    for i in range(1,10):
        if  backup[i]==False:
            return False
    return True
def dfs_c(u,a,c):
    global ans
    if u>9:
        return
    if check(a,c):
        ans+=1
    for i in range(1,10):
        if not st[i]:
            st[i] = True
            dfs_c(u+1,a,c*10+i)
            st[i] = False
def dfs_a(u,a):
    if a>=n:
        return 
    if a:
        dfs_c(u,a,0)
    for i in range(1,10):
        if not st[i]:
            st[i] = True
            dfs_a(u+1,a*10+i)
            st[i] = False

dfs_a(0,0)
print(ans)
