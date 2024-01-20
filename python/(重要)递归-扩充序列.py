def f(n,k):
    part=2 ** (n - 1) - 1
    if k==part+1:
        return n
    elif k<=part:
        return f(n-1,k)
    else:
        return f(n-1,k-part-1)
n,k = map(int,input().split())
print(f(n,k))
