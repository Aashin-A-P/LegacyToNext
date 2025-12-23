ori=[1,2,4,5,7,9,10]
odd=[]
even=[]
for i in ori:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
res=even + odd
print(res)                    
