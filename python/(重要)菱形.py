n = int(input())
for i in range(n):
    for j in range(n):
        if abs(i-(n//2))+abs(j-(n//2)) <= n//2:
           print("*",end = "")
        else:
            print(" ",end = "")
    print()
