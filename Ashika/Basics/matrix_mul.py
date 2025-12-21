n=2
A=[]
B=[]
C=[[0 for _ in range(n)] for _ in range(n)]
res=0
print('A matrix:')
for i in range(0,n):
    row=[]
    for j in range(0,n):
        row.append(int(input()))
    A.append(row)
print('B matrix')
for i in range(0,n):
    row=[]
    for j in range(0,n):
        row.append(int(input()))
    B.append(row)
        
for i in range(len(A)):
    for j in range(n):
        for k in range(n):
            C[i][j]+=A[i][k]*B[k][j]
            
for i in C:
    print(i)