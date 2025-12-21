n=int(input())
a=(n-1)//2
for i in range(1,n+1,2):
    space=' '*a
    print(space+'*'*i)
    a-=1

b=0    
for i in range(n,0,-2):
    space=' '*b
    print(space+'*'*i)
    b+=1

