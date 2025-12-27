from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
A=Counter(myList)
i=list(A.items())
F=[]
for j in range(len(i)):
    F.append(list(i[j]))
print(F)