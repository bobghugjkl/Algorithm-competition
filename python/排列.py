def f(u):
    if u==n:
        for x in path:
            print(x+1,end = ' ')
        print()
    else:
        for i in range(n):
            if not st[i]:
                path[u] = i
                st[i] = True
                dfs(u+1)
                st[i] = False
                path[u] = 0
n = int(input())
path = [0 for i in range(n)]
st = [False for i in range(n)]
f(0)
