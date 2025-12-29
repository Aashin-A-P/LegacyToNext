def bubble(A,n):
    if(n<=1):
        return 
    for i in range(0,n-1):
        if(A[i]>A[i+1]):
            c=A[i]
            A[i]=A[i+1]
            A[i+1]=c
            
    bubble(A,n-1)
    
A=[64,24,12,11,22]
bubble(A,len(A))
for i in A:
    print(i)