n,k = map(int,input().split())
h = []
w = []
for i in range(n):
    w1,h1 = map(int,input().split())
    h.append(w1)
    w.append(h1)
def check(x):
    s = 0
    for i in range(n):
        s = s+(h[i]//x)*(w[i]//x)
        if s>=k:
            return True
    return False
l ,r = 1,10**5
while l<r:
    mid = l+r+1>>1
    if check(mid):
        l = mid
    else:
        r = mid-1
print(l)
