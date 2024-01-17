dic = {'(':0,'+':1,'-':1,'*':2,'/':2}
op = []
num = []
def new_eval():
    b = num.pop()
    a = num.pop()
    c = op.pop()
    if c=='+':
        x = a+b
    elif c=='-':
        x = a-b
    elif c=='*':
        x = a*b
    else:
        x = int(a/b)
    num.append(x)
a = input()
n = len(a)
i = 0
while i<n:
    c = a[i]
    if c.isdigit():
        x = 0
        j = i
        while j<n and a[j].isdigit():
            x = x*10+int(a[j])
            j+=1
        i = j-1
        num.append(x)
    elif c=='(':
        op.append(c)
    elif c==')':
        while op[-1] != '(':
            new_eval()
        op.pop()
    else:
        while len(op) and dic[op[-1]]>=dic[c]:
            new_eval()
        op.append(c)
    i+=1
while len(op):
    new_eval()
print(num[-1])
