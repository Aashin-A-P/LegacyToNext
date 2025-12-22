n=int(input())
a=(n*2)-1
b=2
print(f'{n}'*a)
for i in range(n,1,-1):
    for k in range(n,i-2,-1):
        if(k!=i-1):
            print(f'{k}',end='')
        else: 
            print(f'{k}'*(i-1),end='')
    for j in range(i-1,n+1):
        if(j!=i-1):
            print(f'{j}',end='')
        else: 
            print(f'{j}'*(i-2),end='')
    print()
for i in range(2,n+1):
    for j in range(n,i-1,-1):
        if(j!=i):
            print(f'{j}',end='')
        else:
            print(f'{j}'*j,end='')
    for k in range(j,n+1):
        if(k!=j):
            print(f'{k}',end='')
        else:
            print(f'{k}'*(k-1),end='')
            
    print()
    
 

    
    
        
    
        
    