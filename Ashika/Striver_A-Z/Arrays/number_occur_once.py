nums = [1, 2, 2, 4, 3, 1, 4]
for i in range(0,len(nums)):
    count=0
    for j in range(0,len(nums)):
        if(nums[i]==nums[j]):
            count+=1
    if(count==1):
        print(nums[i])
        