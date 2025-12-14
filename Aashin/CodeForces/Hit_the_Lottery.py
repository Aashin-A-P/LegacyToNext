n = int(input())
l = [100, 20, 10, 5, 1]
c = 0
for i in l:
    c+= n//i
    n = n%i
print(c)