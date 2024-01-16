a,b = input().split()
if len(a) < len(b):
    a,b = b,a
for i in range(len(a)):
    a = a[1:] + a[0]
    if a.find(b) != -1:
        print("true")
        break
else:
    print("false")
