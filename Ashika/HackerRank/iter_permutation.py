from itertools import permutations
name,A=list(input().split(' '))
name=sorted(name)
A=int(A[0])
B=list(permutations(name,A))
for i in B:
    ans=i
    for j in ans:
        print(j,end='')
    print()
        