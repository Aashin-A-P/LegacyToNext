n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
X = a[0]
Y = b[0]
s = set()
for i in range(1,len(a)):
    s.add(a[i])
for i in range(1,len(b)):
    s.add(b[i])
l = list(s)
if(len(l) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")