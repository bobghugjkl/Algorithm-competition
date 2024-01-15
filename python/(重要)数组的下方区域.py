t = input()
a = []
for i in range(12):
    row = list(map(float,input().split()))
    a.append(row)
s,c = 0,0
for i in range(7,12):
    for j in range(12-i,i)
        s+=a[i][j]
        c+=1
if t=="M":
    s/=c
print("%.1f" %s)
