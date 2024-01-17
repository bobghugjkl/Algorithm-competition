def get_unique_count(a,n):
    b=[0 for i in range(2000)]
    count = 0
    for i in a:
        if not b[i]:
            b[i] = 1
            count+=1
    
    print(count)
n = int(input())
a = list(map(int,input().split()))
get_unique_count(a,n)
