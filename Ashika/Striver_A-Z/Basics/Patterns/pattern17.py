n=int(input())
asci=65
a=(n-1)
for i in range(0,n):
    asci=65
    space=' '*a
    print(space,end='')
    for j in range(0,i+1):
        print(f'{chr(asci)}',end='')
        asci+=1
    asci1=(asci-2)    
    for k in range(0,i):
        print(f'{chr(asci1)}',end='')
        asci1-=1
        
    a-=1    
    print()

    