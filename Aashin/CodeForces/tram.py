n = int(input())
cap = 0
new_cap = 0
for i in range(n):
	a,b = map(int,input().split())
	new_cap = new_cap - a + b
	cap = max(cap, new_cap)
print(cap)