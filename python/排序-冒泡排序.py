def bubble_sort(q):
    for i in range(len(q)):
        not_changed = True
        for j in range(len(q) - i - 1):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                not_changed = False
        if not_changed:
            break


n = int(input())
q = list(map(int, input().split()))
bubble_sort(q)

for x in q:
    print(x, end=' ')
