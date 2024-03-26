def f(a,l,r):
    if l>=r:
        return 0
    mid = (l+r)//2
    cnt = f(a,l,mid)+f(a,mid+1,r)
    ans = []
    i = l
    j = mid+1
    while i<=mid and j<=r:
        if a[i]>a[j]:
            cnt+=mid-i+1
            ans.append(a[j])
            j+=1
        else:
            ans.append(a[i])
            i+=1
    ans+=a[i:mid+1]
    ans+=a[j:r+1]
    a[l:r+1] = ans
    return cnt
            

while True:
    cnt = 0
    n = int(input())
    if n==0:
        break
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    print(f(a,0,n-1))
