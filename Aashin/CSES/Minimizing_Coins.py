n, x = map(int,input().split())
l = list(map(int,input().split()))
dp = [0]*n 
for i in l:
	if x%i==0:
		