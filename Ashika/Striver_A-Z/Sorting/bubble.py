A=[64,24,12,11,22]
size=len(A)
for i in range(size):
    j=0
    while(j<size-1):
        if(A[j]>A[j+1]):
            c=A[j]
            A[j]=A[j+1]
            A[j+1]=c
        j+=1
    size-=1
for i in A:
    print(i)