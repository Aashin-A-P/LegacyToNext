A=[24,34,65,1,17]
maxa=A[0]
for i in range(len(A)):
    if(maxa<A[i]):
        maxa=A[i]
print(f'max: {maxa}')