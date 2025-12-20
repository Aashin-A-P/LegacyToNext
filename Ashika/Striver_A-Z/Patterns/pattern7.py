n=int(input())
a=(n-1)//2

for i in range(1,n+1,2):
    space=' '*a
    print(space+'*'*i,end='')
    print()
    a=(a-1)
    
