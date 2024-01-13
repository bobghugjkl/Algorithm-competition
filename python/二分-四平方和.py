def cal():
    for a in range(int(n**0.5+1)):
        for b in range(a,int(n**0.5+1)):
            t = n-a*a-b*b
            if t in dic:
                c,d = dic[t]
                print(a,b,c,d)
                return
            

dic = {}
n = int(input())
for c in range(int(n**0.5+1)):
    for d in range(c,int(n**0.5+1)):
        if c*c + d*d not in dic:
            dic[c*c+d*d]=[c,d]
cal()
        
