def max123(x,y):
    if x>y:
        return x
    else:
        return y
##################################
print(max123(1,2))
print(max123(20,10))
print(max123(10,10))

def sum123(nums):
    result = 0
    for n in nums:
        result+=n
    return result
###################################
print(sum123([10,20,30,40,50]))