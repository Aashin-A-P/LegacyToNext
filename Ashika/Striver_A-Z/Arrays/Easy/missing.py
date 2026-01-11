nums = [1, 3, 6, 4, 2, 5]
le=len(nums)
nums.sort()
l=0
for i in range(len(nums)):
    if(i!=nums[l]):
        print(i)
        l-=1
    l+=1
    
if(le!=nums[le-1]):
    print(le)