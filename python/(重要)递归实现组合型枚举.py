n,m=map(int,input().split())
vis=[0 for i in range(n+1)]
st =[0 for i in range(n+1)]

def dfs(x):
    if x>=m:
        for i in range(m):
            print(st[i],end=' ')
        print('')
        return

    for i in range(1,n+1):
        if vis[i]==0 and (x==0 or i>st[x-1]):
            vis[i]=1
            st[x]=i
            dfs(x+1)
            vis[i]=0

dfs(0)
