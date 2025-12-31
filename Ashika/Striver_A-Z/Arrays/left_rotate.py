A=[1,17,23,45]
val=A[0]
for i in range(0,len(A)-1):
    A[i]=A[i+1]
A.remove(A[len(A)-1])
A.append(val)
for i in A:
    print(i)
        
