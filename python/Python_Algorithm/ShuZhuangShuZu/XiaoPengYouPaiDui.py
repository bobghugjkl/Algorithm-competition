def lowbit(x):
    return x & (-x)


def add(x, val):
    while x < 1000010:
        b[x] += val
        x += lowbit(x)


def query(x):
    res = 0
    while x:
        res += b[x]
        x -= lowbit(x)
    return res


N = 1000010
b = [0] * int(1000010)
n = int(input().split())
res = [0] * n
nums = list(map(int, input().split()))
for i in range(n):
    res[i] += query(N - 1) - query(nums)
    add(nums[i] + 1, 1)
b = [0] * int(N)
for i in range(n - 1, -1, -1):
    res[i] += query(nums[i])
    add(nums[i] + 1, 1)
ans = 0
for a in res:
    ans += (a + 1) * a // 2
print(ans)
