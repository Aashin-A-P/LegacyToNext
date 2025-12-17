n = int(input())
for i in range(n+1):
    for j in range(i):
        if (i+j)%2==0:
            print(0,end= '')
        else:
            print(1,end='')
    print()
        