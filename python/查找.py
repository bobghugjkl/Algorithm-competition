n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = map(int,input().split())
for i in b:
    if i in a:
        print("YES")
    else:
        print('NO')
