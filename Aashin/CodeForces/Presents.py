n = int(input())
a = list(map(int,input().split()))
d = dict()
res = []
for i in range(1,n+1):
	d[a[i-1]] = i
for i in range(1,n+1):
	print(d[i],end=" ")