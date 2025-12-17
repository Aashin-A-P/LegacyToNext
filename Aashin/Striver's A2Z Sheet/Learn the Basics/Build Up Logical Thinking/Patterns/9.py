n = int(input())
a = 1
for i in range(n-1,-1,-1):
    print(i*' ' + a * '*')
    a+=2
    print()
a = 2 * (n-1) + 1
for i in range(n):
    print(i*' ' + a * '*')
    print()
    a = a - 2