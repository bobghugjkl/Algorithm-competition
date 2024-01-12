a, b, c = map(float, input().split())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a * a == b * b + c * c:
        print("TRIANGULO RETANGULO")
    if a * a > b * b + c * c:
        print("TRIANGULO OBTUSANGULO")
    if a * a < b * b + c * c:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:  # 等价于 a == b and b == c
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c:
        print("TRIANGULO ISOSCELES")

作者：yxc
链接：https://www.acwing.com/activity/content/code/content/6997443/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
