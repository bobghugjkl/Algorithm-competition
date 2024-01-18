dic = {}
n = int(input())
for x in map(int,input().split()):
    if x not in dic:
        dic[x] = 0
    dic[x] += 1
rk,rv = 0,0
for k,v in dic.items():
    if v>rv or v==rv and k<rk:
        rk,rv = k,v
print(rk)
