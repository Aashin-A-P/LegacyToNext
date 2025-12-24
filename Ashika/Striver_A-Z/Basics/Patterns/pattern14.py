n=int(input())
asci=65
for i in range(0,n):
    asci=65
    for j in range(0,i+1):
        print(chr(asci),end='')
        asci+=1
    print()
    
        