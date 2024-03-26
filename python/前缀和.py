N = 100010
n,m = map(int(input()))
a = [0]*N
s = [0]*N
a[1:n+1] = list(map(int,input().split()))
for i in range(1,n+1):
	s[i] = s[i-1]+a[i]
while m:
	l,r = map(int,input().split())
	print(s[r]-s[l-1])
	m-=1
