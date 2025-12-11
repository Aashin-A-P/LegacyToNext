a = input()
l = []
for i in a:
	l.append(i)
b = set(l)
c = len(b)
if c%2==0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")