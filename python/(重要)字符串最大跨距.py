s,s1,s2 = input().split(',')
x1 = s.find(s1)
x2 = s.rfind(s2)
dist = x2-x1-len(a)
if x1==-1 or x2==-1 or dist<0:
    print("-1")
else:
    print(dist)
