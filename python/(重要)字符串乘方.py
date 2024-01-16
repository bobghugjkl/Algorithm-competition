while True:
    n = input()
    if n=='.':
        break
    s = len(n)
    for i in range(1,s+1):
        if s%i == 0:
            t =""
            for j in range(s//i):
                t+=n[:i]
                
            if t==n:
                print(s//i)
                break
