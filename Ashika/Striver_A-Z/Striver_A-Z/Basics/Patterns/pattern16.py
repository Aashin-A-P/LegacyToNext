n=int(input())
asci=64
for i in range(0,n):
    asci+=1
    for j in range(0,i+1):
        print(chr(asci),end='')
        
    print()

    
    