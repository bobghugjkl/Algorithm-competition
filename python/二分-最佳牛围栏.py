from math import floor

eps = 1e-5
def check(x) : # 是否能找到满足平均值大于等于x的区间（扫描区间）/优化求最大子段和是否大于mid
    s = [0] * (n + 1)
    for i in range(1, n + 1) :
        s[i] = s[i - 1] + a[i] - x
    minnv = 10000000010
    res = -10000000010
    for i in range(m, n + 1) :
        minnv = min(minnv, s[i - m])
        res = max(res, s[i] - minnv)
    return res >= 0

n, m = map(int, input().split())

a = [0] * (n + 1)
for i in range(1, n + 1) :
    a[i] = int(input())

l, r = 1, 2000

while l + eps < r :
    mid = (l + r) / 2
    if check(mid) :
        l = mid
    else :
        r = mid
print(floor(r * 1000))
