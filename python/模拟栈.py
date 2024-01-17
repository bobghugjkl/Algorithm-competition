n = int(input())
res =[]
while n:
    li = input().split()
    if li[0]=='push':
        res.append(int(li[1]))
    elif li[0] == 'pop':
        res.pop()
    elif li[0] == 'empty':
        if len(res) == 0:
            print("YES")
        else:
            print("NO")
    else:
        print(res[-1])
    n -= 1
