n=int(input())
A=[0 for _ in range(n) ]
for i in range(n):
    A[i]=(int(input()))

for i in range(n):
    count=0
    for j in range(n):
        if(A[i]==A[j]):
            count+=1
    if(count==1):
        print(A[i],end=' ')