def inser(A,n):
    if(n<=1):
        return 
    inser(A,n-1)
    k=A[n-1]
    j=n-2
    while(j>=0 and A[j]>k):
        A[j+1]=A[j]
        j-=1
    j+=1
    if(k!=A[j]):
        A[j]=k
        
A=[65,24,12,22,11]
inser(A,len(A))
for i in A:
    print(i)