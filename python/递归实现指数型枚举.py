def dfs(u):
    if u==n:
        for i in range(n):
            if st[i] == 1:
                print(i+1,end = ' ')
        print()
        return
    else:
        st[u] = 2
        dfs(u+1)
        
        st[u] = 1
        dfs(u+1)
        st[u] = 0
n = int(input())
st = [0 for i in range(n)]

dfs(0)
