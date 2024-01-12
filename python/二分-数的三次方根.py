def binary_search(n):
    low = -10000
    high = 10000
    while high - low > 1e-8:
        mid = (low + high)/2
        if mid * mid * mid < n:
            low = mid
        else:
            high = mid
    return low
n = float(input())
print("%.6f"%(binary_search(n)))
