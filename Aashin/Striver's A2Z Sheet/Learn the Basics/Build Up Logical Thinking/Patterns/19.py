s = 0
for i in range(5,0,-1):
    for j in range(i):
        print('*', end='')
    for j in range(s):
        print(' ', end = '')
    for j in range(i):
        print('*', end='')
    print()
    s+=2
s-=2
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    for j in range(s):
        print(' ', end = '')
    for j in range(i):
        print('*', end='')
    print()
    s-=2

    