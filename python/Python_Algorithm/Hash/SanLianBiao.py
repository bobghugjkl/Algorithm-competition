#字典
n = int(input())
s = set()
for i in range(n):
    a,b = input().split()
    b = int(b)
    if a == 'I':
        s.add(b)
    else:
        if b in s:
            print("Yes")
        else:
            print("No")