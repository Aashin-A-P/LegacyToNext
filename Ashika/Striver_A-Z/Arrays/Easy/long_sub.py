nums = [-3, 2, 1]
k=6
e=0
maxa=0
for i in range(0,len(nums)):
    s=0
    e=0
    for j in range(i,len(nums)):
        if(s<15):
            s+=nums[j]
            e+=1
    if(maxa<e and s==15):
        maxa=e
print(f'{maxa}')