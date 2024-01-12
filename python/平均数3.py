a, b, c, d = map(float, input().split())
x = (a * 2 + b * 3 + c * 4 + d) / 10
print("Media: %.1f" % x)

if x >= 7:
    print("Aluno aprovado.")
elif x < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    y = float(input())
    print("Nota do exame: %.1f" % y)
    z = (x + y) / 2
    if z >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % z)

作者：yxc
链接：https://www.acwing.com/activity/content/code/content/6997515/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
