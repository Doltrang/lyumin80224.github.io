nums  = [2,1,5,4,7,8,6]
nums2 = [] #挑奇數置入
for n in nums:
    # if n%2==1: #餘數1=true 0=flase
    if n%2:
        nums2.append(n)
print(nums2)

print([n for n in nums if n % 2])