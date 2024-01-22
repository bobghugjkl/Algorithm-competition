def quick_sort(q,l,r):
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
    quick_sort(q,l,j)
    quick_sort(q,j+1,r)

n = int(input())
q = list(map(int,input().split()))
quick_sort(q,0,n-1)
for i in q:
    print(i,end = " ")
    
