n = int(input())
a = 2 * (n-1) + 1
for i in range(n):
    print(i*' ' + a * '*')
    print()
    a = a - 2