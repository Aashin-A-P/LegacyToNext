n = int(input())
a = ['I hate','I love']
s = ''
i = n
for i in range(n-1):
	s = s+ a[i%2] + ' that '
s = s + a[(i+1)%2] + ' it'
print(s)