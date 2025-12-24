def rev(n,s=0,e=None):
    if(e==None):
        e=len(n)-1
    if(s>=e):
        return
    n[s],n[e]=n[e],n[s]
    rev(n,s+1,e-1)
    
n=int(input())
A=[0 for _ in range(n)]
for i in range(n):
    A[i]=int(input())

rev(A)
for i in A:
    print(i)
