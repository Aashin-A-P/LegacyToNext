A=[65,24,12,22,11]
for i in range(len(A)):
    key=A[i]
    j=i-1
    while(j>=0 and A[j]>key):
        A[j+1]=A[j]
        j-=1
    j+=1
    if(key!=A[j]):
        A[j]=key
        
for i in A:
    print(i)