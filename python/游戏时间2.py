a,b,c,d = map(int,input().split())
if (c-a<=0 and d-b<=0) or c-a<0:
    endhour = 24+(c-a)
else:
    endhour = c-a
if d-b<0:
    endminutes = 60+(d-b)
    endhour-=1
else:
    endminutes = d-b
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(endhour,endminutes))
