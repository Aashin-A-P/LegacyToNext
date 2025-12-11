a = []
for i in range(5):
	n = list(map(int,input().split()))
	a.append(n)
for i in range(5):
	for j in range(5):
		if a[i][j] == 1:
			x,y = i,j
res = abs(x-2)+abs(y-2)
print(res)
