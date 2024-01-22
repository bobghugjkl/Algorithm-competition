def merge_sort(q,l,r):
    if l>= r:
        return
    mid = (l+r)//2
    merge_sort(q,l,mid)
    merge_sort(q,mid+1,r)
    tmp = []
    i = l
    j = mid+1
    while i<=mid and j<=r:
        if q[i]<=q[j]:
            tmp.append(q[i])
            i+=1
        else:
            tmp.append(q[j])
            j+=1
    tmp += q[i:mid+1]
    tmp += q[j:r+1]
    q[l:r+1] = tmp
    
n = int(input())
q = list(map(int,input().split()))
merge_sort(q,0,n-1)
for i in q:
    print(i,end = " ")
