n=int(input())
asci=65+(n)+1
for i in range(0,n):
    asci-=1
    asci2=asci
    for j in range(0,i+1):
        print(chr(asci2),end='')
        asci2+=1
        
    print()