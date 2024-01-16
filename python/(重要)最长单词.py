s = input()
b = len(s)
s = s[:b-1]
a = s.split()
t = ""
for i in a:
    if len(i)>len(t):
        t = i
print(t)
