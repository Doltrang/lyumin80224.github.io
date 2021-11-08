def check(n):
    if n>4:
        return 2.5
    else:
        return n
###############################
nums=[2,3,1,6,5,8,7,4]
print(sorted(nums))
print(sorted(nums,key=check))