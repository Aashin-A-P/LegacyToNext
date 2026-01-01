nums = [0, 1, 4, 0, 5, 2]
for i in nums:
    if(i==0):
        nums.remove(i)
        nums.append(i)
print(nums)