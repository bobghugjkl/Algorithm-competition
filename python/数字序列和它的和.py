while True:
    m,n = map(int,input().split())
    if m>n:
        m,n = n,m
    if m<=0 or n<=0:
        break
    else:
        cnt = 0
        for i in range(m,n+1):
            print(i,end=" ")
            cnt+=i
        print("Sum=%d"%(cnt))
