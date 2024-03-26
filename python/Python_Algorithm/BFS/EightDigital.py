from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(start):
    end = "12345678x"
    d = {start: 0}
    q = deque([start])
    while (len(q)):
        t = q.popleft()
        distance = d[t]
        if t == end:
            return distance
        idx = t.find('x')
        x = idx // 3
        y = idx % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                t = list(t)  # 字符串不能交换要先换成列表再交换
                t[idx], t[a * 3 + b] = t[a * 3 + b], t[idx]
                t = ''.join(t)
                if t not in d:
                    d[t] = distance + 1
                    q.append(t)
                t = list(t)
                t[idx], t[a * 3 + b] = t[a * 3 + b], t[idx]  # 恢复一下
                t = ''.join(t)
    return -1


n = input().split()
start = ''
for c in n:
    start += c
print(bfs(start))
