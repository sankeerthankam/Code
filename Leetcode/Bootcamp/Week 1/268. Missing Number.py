def missingNumber(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1 and nums[0] == 0:
        return 1
    else:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
                
# Find the sum of n numbers 
# Subtract the sum of the current array
# Type caset the result to int and return the result

def missingNumber(nums):
    l = len(nums)
    return int((l*(l+1))/2 - sum(nums))
