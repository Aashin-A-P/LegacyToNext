n=int(input())
a=(n-1)
for i in range(1,n+1):
    print('*'*i,end='')
    space=' '*a*2
    print(space,end='')
    print('*'*i)
    a-=1

b=1
for i in range(n-1,0,-1):
    print('*'*i,end='')
    space=' '*b*2
    print(space,end='')
    print('*'*i)
    b+=1