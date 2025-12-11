n = int(input())
count = 0
for i in range(n):
	a = map(int,input().split())
	if sum(a)>1:
		count+=1
print(count)