def f(q,l,r,k):
    if l>=r:
        return q[l]
    i = l-1
    j = r+1
    x = q[(l+r)//2]
    while i<j:
        while True:
            i+=1
            if q[i]>=x:
                break
        while True:
            j-=1
            if q[j]<=x:
                break
        if i<j:
            q[i],q[j] = q[j],q[i]
    if j+1-l>=k:
        return f(q,l,j,k)
    else:
        return f(q,j+1,r,k-(j-l+1))

n,k = map(int,input().split())
q = list(map(int,input().split()))
print(f(q,0,n-1,k))
