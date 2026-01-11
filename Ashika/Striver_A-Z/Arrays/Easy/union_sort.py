nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
for i in nums2:
    if i not in nums1:
        nums1.append(i)
print(nums1)