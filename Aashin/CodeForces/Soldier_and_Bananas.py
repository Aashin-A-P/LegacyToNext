k,n,w = map(int,input().split())
required = ((w*(w+1))//2) * k
if required > n:
	print(required-n)
else:
	print(0)