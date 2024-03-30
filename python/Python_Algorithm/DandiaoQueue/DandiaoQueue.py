N = 1000010
hh, tt = 0, -1
res = [0] * N
n, k = input().split()
k = int(k)
li = list(map(int, input().split()))

for i in range(len(li)):
    while hh <= tt and i - k + 1 > res[hh]:
        hh += 1
    while hh <= tt and li[res[tt]] > li[i]:
        tt -= 1
    tt += 1
    res[tt] = i
    if i >= k - 1:
        print(li[res[hh]], end=" ")
print()

hh, tt = 0, -1
for i in range(len(li)):
    while hh <= tt and i - k + 1 > res[hh]:
        hh += 1
    while hh <= tt and li[res[tt]] < li[i]:
        tt -= 1
    tt += 1
    res[tt] = i
    if i >= k - 1:
        print(li[res[hh]], end=" ")
print()
