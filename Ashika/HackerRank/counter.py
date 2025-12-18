from collections import defaultdict,Counter
num=int(input())
A=list(map(int,input().split(' ')))
cus=int(input())
C=Counter(A).items()
key=list(Counter(A).keys())
val=list(Counter(A).values())
tot=0
for i in range(cus):
    size,price=map(int,input().split())
    for j in range(len(key)):
        if(size==key[j]):
            if(val[j]==0):
                break
            
            tot+=price
            val[j]-=1
            

print(tot)