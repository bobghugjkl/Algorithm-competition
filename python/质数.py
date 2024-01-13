n = int(input())
for i in range(n):
    x = int(input())
    flag = 1
    for j in range(2,int(x**0.5+1)):
        if x%j==0:
            flag = 0
            break
    if flag == 1:
        print("%d is prime" %(x))
    else:
        print("%d is not prime" %(x))
