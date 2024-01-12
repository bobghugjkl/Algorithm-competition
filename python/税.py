x = float(input())

tot = 0

if x > 4500:
    tot += (x - 4500) * 0.28
    x = 4500

if x > 3000:
    tot += (x - 3000) * 0.18
    x = 3000

if x > 2000:
    tot += (x - 2000) * 0.08
    x = 2000

if tot == 0:
    print("Isento")
else:
    print("R$ %.2f" % tot)
