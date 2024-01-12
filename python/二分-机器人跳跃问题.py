def check(x):
    for i in range(n):
        x = 2*x-a[i]
        if x<0:
            return 0
    return 1


def f(a):
    l,r = 0,10**5+1
    while l<r:
        mid = int((l+r)/2)
        if(check(mid)==0):
            l=mid+1
        else:
            r=mid
    return l



n = int(input())
a = list(map(int,input().split()))
print(f(a))
