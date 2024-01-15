while True:
    n = int(input())
    if n==0:
        break
    for i in range(n):
        for j in range(n):
            print(abs(j-i)+1,end = ' ')
        print()
    print() 
