n = float(input())
n = int(n * 100)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % (n // 10000))
n %= 10000
print("%d nota(s) de R$ 50.00" % (n // 5000))
n %= 5000
print("%d nota(s) de R$ 20.00" % (n // 2000))
n %= 2000
print("%d nota(s) de R$ 10.00" % (n // 1000))
n %= 1000
print("%d nota(s) de R$ 5.00" % (n // 500))
n %= 500
print("%d nota(s) de R$ 2.00" % (n // 200))
n %= 200

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % (n // 100))
n %= 100
print("%d moeda(s) de R$ 0.50" % (n // 50))
n %= 50
print("%d moeda(s) de R$ 0.25" % (n // 25))
n %= 25
print("%d moeda(s) de R$ 0.10" % (n // 10))
n %= 10
print("%d moeda(s) de R$ 0.05" % (n // 5))
n %= 5
print("%d moeda(s) de R$ 0.01" % n)
