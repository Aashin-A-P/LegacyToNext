A=[65,24,12,22,11]
for i in range(len(A)):
    key=A[i]
    mina=A[i]
    for j in range(i+1,len(A)):
        if(A[j]<mina):
            mina=A[j]
            ind=j
    if(mina!=key):
        A[i]=mina
        A[ind]=key
        
for i in A:
    print(i)
            