def dfs(u):
    if u>n:
        for i in st[1:]:
            print(i,end = " ")
        print()
        return
    for i in range(1,n+1):
        if used[i] == False:
            st[u] = i
            used[i] = True
            dfs(u+1)
            used[i] = False

n = int(input())
st = [0 for i in range(n+1)]
used = [False for i in range(n+1)]
dfs(1)
