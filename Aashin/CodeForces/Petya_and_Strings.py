a = input()
b = input()
a = a.lower()
b = b.lower()
flag = 0
for i in range(len(a)):
	if a[i]<b[i]:
		print(-1)
		flag = 1
		break
	if a[i]>b[i]:
		print(1)
		flag = 1
		break
if flag==0:
	print(0)