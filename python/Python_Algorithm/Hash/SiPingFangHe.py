from copy import deepcopy

n = int(input())
maxn = int(5e6) + 10
dic = dict()
for a in range(maxn):
    if a * a > n:
        break
    for b in range(a, maxn):
        if a * a + b * b > n:
            break
        if dic.get(a * a + b * b) is None:
            dic[a * a + b * b] = (a, b)
ans = [maxn for _ in range(4)]
for a in sorted(dic.keys()):
    b = n - a
    if a > b:
        break
    if b in dic.keys():
        tmp = list(dic[a] + dic[b])
        tmp.sort()
        for i in range(4):
            if tmp[i] != ans[i]:
                if tmp[i] < ans[i]:
                    ans = deepcopy(tmp)
                break
for i in range(3):
    print(ans[i], end=' ')
print(ans[-1])

'''
import math
N = 5000010
C = [-1] *N
D = [-1] *N
n = int(input())
for c in range(int(math.sqrt(n))+1):
    for d in range(c,int(math.sqrt(n - c*c))+1):
        s = c*c + d*d
        if C[s] == -1:
            C[s] = c
            D[s] = d
flag = False
for a in range(int(math.sqrt(n))+1):
    for b in range(a,int(math.sqrt(n - a*a))+1):
        s = n - a*a-b*b
        if C[s] != -1:
            print(a,b,C[s],D[s])
            flag = True
            break
        else:
            continue
    if flag == True:    
        break
'''
