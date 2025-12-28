A=[65,24,12,22,11]
for i in range(len(A)):
    key=A[i]
    j=i-1
    k=i
    while(j>=0 and key<A[j]):
        A[j+1]=A[j]
        j-=1
    if(i!=j):
        j+=1
        A[j]=key

for i in A:
    print(i)