n = int(input())
s = input()
a = 0
for i in s:
	if i=='A':
		a+=1
	else:
		a-=1
if a>0:
	print('Anton')
elif a==0:
	print('Friendship')
else:
	print('Danik')