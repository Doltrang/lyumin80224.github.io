nums  =[10,20,30]
nums2 =[]
for n in nums:
    nums2.append(n**2)
print(nums2)

print([n**2 for n in nums])

print(sum([int(x) for x in input('輸入任意數個數字以空白分隔').split()]))