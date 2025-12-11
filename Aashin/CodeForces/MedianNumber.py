n = int(input())
for i in range(n):
	a = list(map(int,input().split()))
	a = sorted(a)
	print(a[1])