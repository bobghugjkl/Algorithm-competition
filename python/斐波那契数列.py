n = int(input())
a,b = 0,1
if n==1:
    print(a)
elif n==2:
    print("%d %d"%(a,b))
else:
     print("%d %d"%(a,b),end=" ")
     for i in range(3,n+1):
         print(a+b,end=" ")
         a,b=b,a+b
    
