n=int(input())
asci=65
for i in range(n,0,-1):
    asci=65
    for j in range(0,i):
        print(chr(asci),end='')
        asci+=1
    print()
    