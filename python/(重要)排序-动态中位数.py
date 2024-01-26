import heapq

n = int(input())
for i in range(n):
    down,up = [],[]
    num, m = map(int,input().split())
    size = (m+1)//2
    print(num,size)
    count = 0
    q = [] #记录所有输入
    while count < m:
        a = list(map(int,input().split()))
        q += a
        count += len(a)
    #利用大小根堆将数分为两组
    cnt = 0
    for each in q:
        if len(down) == 0 or each <= -down[0]: heapq.heappush(down,-each)  #利用相反数加小根堆实现大根堆
        else: heapq.heappush(up, each)
        if len(down) >len(up)+1 :heapq.heappush(up, -heapq.heappop(down))
        if len(up) > len(down): heapq.heappush(down, -heapq.heappop(up))

        cnt += 1
        if cnt % 2:
            if cnt == 21:
                print()
                cnt -= 20
            print(-down[0]  ,end= ' ')

    print(' ')

