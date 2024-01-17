def sort(a,l,r):
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            if a[j]<a[i]:
                a[i],a[j] = a[j],a[i]

n,l,r = map(int,input().split())
a = list(map(int,input().split()))
sort(a,l,r)
for x in a:
    print(x,end=' ')
