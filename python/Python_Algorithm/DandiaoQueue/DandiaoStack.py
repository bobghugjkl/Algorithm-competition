n = int(input())
li = list(map(int, input().split()))
ans = []
res = []
for i in li:
    if not res:
        res.append(i)
        ans.append(str(-1))
        continue
    else:
        while i <= res[-1]:
            res.pop()
            if not res:
                ans.append(str(-1))
                res.append(i)
                break
        else:
            ans.append(str(res[-1]))
            res.append(i)
print(" ".join(ans))
