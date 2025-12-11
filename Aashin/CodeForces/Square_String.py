n = int(input())
for i in range(n):
	s= input()
	l = len(s) + 1
	if s[:l//2]==s[l//2:]:
		print('YES')
	else:
		print('NO')