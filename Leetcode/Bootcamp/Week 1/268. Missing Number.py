# Approach 1:
# Create a list of len(l) 
# Traverse through the list and return the missing number
def missingNumber(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1 and nums[0] == 0:
        return 1
    else:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

            
# Approach 2:
# Create a list of len(l) 
# Calculate the sum of new_list
# Subtract the sum of input list from sum of new_list
# Return the difference

def missing(nums):
    return sum([i for i in range(len(nums)+1)]) - sum(nums)
    
# Approach 3:
# Find the sum of n numbers 
# Subtract the sum of the current array
# Type caset the result to int and return the result

def missingNumber(nums):
    l = len(nums)
    return int((l*(l+1))/2 - sum(nums))
