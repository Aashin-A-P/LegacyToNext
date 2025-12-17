from collections import defaultdict
d=defaultdict(list)
a=input()
n,m=map(int,a.split(' '))
A=[]
B=[]
for i in range(0,n):
    A.append(input())
    
for j in range(0,m):
    B.append(input())

for i in range(len(A)):
    d[A[i]].append(i+1)
    
for j in range(len(B)):
    pos=d[B[j]]
    if(pos):
        print(' '.join(map(str,pos)),end=' ')
    else:
        print(-1,end='')
    print()