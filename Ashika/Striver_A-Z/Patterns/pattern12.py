n=int(input())
a=(n-1)
for i in range(1,n+1):
    space=' '*a
    for j in range(1,i+1):
        print(f'{j}',end='')
    print(space+space,end='')
    for k in range(i,0,-1):
        print(f'{k}',end='')
    a-=1
    print()
    
    