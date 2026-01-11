nums = [1, 3, 5, -7, 6, -3]
target = 0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            print(f'[{i},{j}]')
            break
    