n = 4
s = 6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    for j in range(s):
        print(" ", end = '')
    for j in range(i,0,-1):
        print(j, end='')
    s-=2
    print()