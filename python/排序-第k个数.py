def f(q,l,r):
    if l>=r:
        return
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
    f(q,l,j)
    f(q,j+1,r)
n,k = map(int,input().split())
q = list(map(int,input().split()))
f(q,0,n-1)
print(q[k-1])
