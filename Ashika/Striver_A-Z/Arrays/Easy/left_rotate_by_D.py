nums = [1,2,3,4,5,6]
k=3
new=[]
for i in range(0,k):
    new.append(nums[0])
    nums.remove(nums[0])
for i in new:
    nums.append(i)
print(nums)
    
    