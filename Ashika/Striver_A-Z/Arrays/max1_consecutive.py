nums = [1, 1, 0, 0, 1, 1, 1, 0]
val=0
ans=0
for i in nums:
    if(i):
        val+=1
        if(val>ans):
            ans=val
            
    else:
        val=0
print(ans)