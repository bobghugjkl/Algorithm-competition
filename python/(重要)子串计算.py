from sys import stdin

for s in stdin.readlines():
    cnt = {}
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            t = s[i:j]
            if t not in cnt:
                cnt[t] = 0
            cnt[t]+=1
    for k in sorted(cnt):
        if cnt[k]>1:
            print(k,cnt[k])
