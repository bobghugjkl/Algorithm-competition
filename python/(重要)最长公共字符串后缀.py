while True:
    n = int(input())
    if n==0:
        break
    a = []
    for i in range(n):
        a.append(input())
    for k in range(len(a[0]),-1,-1):
        suffix = a[0][-k:] if k>0 else ""
        for s in a:
            if not s.endswith(suffix):
                break
        else:
                print(suffix)
                break
