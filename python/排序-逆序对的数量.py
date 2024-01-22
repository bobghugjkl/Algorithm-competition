def f(q,l,r):
    if l>=r:
        return 0
    mid = (l+r)//2
    
    ans = f(q,l,mid)+f(q,mid+1,r)
    tmp = []
    i = l
    j = mid+1
    while i<=mid and j<=r:
        if q[i]>q[j]:
            tmp.append(q[j])
            ans+=mid-i+1
            j+=1
        else:
            tmp.append(q[i])
            i+=1
    tmp+=q[i:mid+1]
    tmp+=q[j:r+1]
    q[l:r+1] = tmp
    return ans
n = int(input())
ans = 0
q = list(map(int,input().split()))
print(f(q,0,n-1))
