l = list(map(int,input().split()))
n = l[0]
m = l[1]
flag = 0
for i in range(n):
    if i%2!=0:
        flag = abs(flag-(m-1))
    for j in range(m):
        if i%2==0:
            print('#',end='')
        else:
            if j == flag:
                print('#',end='')
            else:
                print('.',end='')
    print()