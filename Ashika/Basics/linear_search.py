n=int(input())
A=[0 for _ in range(n) ]
for i in range(n):
    A[i]=(int(input()))
print('key: ',end='')
val=int(input())
for i in range(n):
    if(val==A[i]):
        print('element found')