# Approach 1
# Traverse through the array and count the number of consecutive occurance usning 'cnt' variable.
# Reset the 'cnt' to 0 when you encounter 0
# Store and update the max_so_far with 'max_' variable. 

def findMaxConsecutiveOnes(nums):
    cnt = 0
    max_ = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
            max_ = max(max_, cnt)
        else:
            cnt = 0
    return max_
