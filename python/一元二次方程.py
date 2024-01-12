a, b, c = map(float, input().split())

dt = b * b - 4 * a * c

if dt < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + dt ** 0.5) / (2 * a)
    r2 = (-b - dt ** 0.5) / (2 * a)
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)
