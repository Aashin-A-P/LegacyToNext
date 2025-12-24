n=int(input())
space=' '*(n-2)
print('*'*n)
for j in range(1,n-1):
    print('*',end='')
    print(space,end='')
    print('*')
print('*'*n)
        
    