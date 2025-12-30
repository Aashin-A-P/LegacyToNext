def merge(A,l,m,r):
    n1=m-l+1
    n2=r-m
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=A[l+i]
    for j in range(n2):
        R[j]=A[m+1+j]
    i,j,k=0,0,l
    while(i<n1 and j<n2):
        if(L[i]<R[j]):
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while(i<n1):
        A[k]=L[i]
        i+=1
        k+=1
    while(j<n2):
        A[k]=R[j]
        j+=1
        k+=1
        
def mergeSort(A,l,r):
    if(l<r):
        m=(l+r)//2
        mergeSort(A,l,m)
        mergeSort(A,m+1,r)
        merge(A,l,m,r)

A=[65,24,12,22,11]
mergeSort(A,0,len(A)-1)
for i in A:
    print(i)