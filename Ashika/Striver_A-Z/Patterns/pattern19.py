n=int(input())
a=0
for i in range(n,0,-1):
    print('*'*i,end='')
    space=' '*a
    print(space,end='')
    print('*'*i)
    a+=2
b=(a-2)
for i in range(1,n+1):
    print('*'*i,end='')
    space=' '*b
    print(space,end='')
    print('*'*i)
    b-=2
    