def sum122(nums):
    result = 0
    for n in nums:
        result+=n
    return result
def sum123(*nums):
    result = 0
    for n in nums:
        result+=n
    return result
###################################
print(sum122([10,20,30,40,50]))
print(sum123(10,20,30,40,50))