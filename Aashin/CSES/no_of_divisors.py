def no_of_divisors(n):
	count = 1
	for i in range(1,n//2+1):
		if n%i==0:
			count+=1
	return count

n = int(input())
for i in range(n):
	num = int(input())
	print(no_of_divisors(num))