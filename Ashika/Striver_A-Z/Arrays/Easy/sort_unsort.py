A=[1,17,23,45]
ans=1
for i in range(len(A)-1):
    if(A[i]>A[i+1]):
        ans=0
        break
val=bool(ans)
print(val)