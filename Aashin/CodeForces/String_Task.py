a = input()
s = "" 
for i in a:
	if i in "AEIOUaeiou":
		pass
	else:
		s+="."
		s+=i
print(s.toLowerCase())