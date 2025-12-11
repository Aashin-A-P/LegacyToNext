n = int(input())
c = 1
for i in range(n):
	a = input()
	if i == 0:
		s = a 
	if a != s:
		s = a 
		c+=1
print(c)