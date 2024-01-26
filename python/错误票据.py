def f(q,l,r):
    if l>=r:
        return
    mid = (l+r)//2
    f(q,l,mid)
    f(q,mid+1,r)
    i = l
    j = mid+1
    a = []
    while i<=mid and j<=r:
        if q[i]>q[j]:
            a.append(q[j])
            j+=1
        else :
            a.append(q[i])
            i+=1
    a+=q[i:mid+1]
    a+=q[j:r+1]
    q[l:r+1] = a
n = int(input())
tmp = []
while n>0:
    q = list(map(int,input().split()))
    n-=1
    tmp+=q[:]

f(tmp,0,len(tmp)-1)

cnt1 = 0
cnt2 = 0
for i in range(len(tmp)-1):
    j = i+1
    if tmp[i]==tmp[j]:
        cnt2 = tmp[i]
    if tmp[i]==tmp[j]-2:
        cnt1 = tmp[i]+1
print(cnt1,end = " ")
print(cnt2)
