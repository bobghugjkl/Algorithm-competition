while True:
    n = int(input())
    if n==0:
        break
    for i in range(n):
        for j in range(n):
            print(2**(i+j),end = ' ')
        print()
    print()
