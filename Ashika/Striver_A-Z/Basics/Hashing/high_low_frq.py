from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
A=Counter(myList)
print(A)
ans=max(A,key=A.get)
ans1=min(A,key=A.get)
print(f'high: {ans}')
print(f'low: {ans1}')