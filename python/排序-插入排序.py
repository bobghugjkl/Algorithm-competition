def insertion_sort(q):
    for i in range(len(q)):
        j = i
        while j>0 and q[j]<q[j-1]:
            q[j-1],q[j] = q[j],q[j-1]
            j-=1

n = int(input())
q = list(map(int,input().split()))
insertion_sort(q)
for x in q:
    print(x,end = " ")
