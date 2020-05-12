# Approach 1:
# Use two pointer p1 and p2
# While p2 < len(nums)
  # Compare two elements next to each other and remove if they are equal.
  # Once you remove the element in place, the size of the array also decreases, hence update l = l - 1 
  # Do not increment the pointers here, since you have already deleted the element in place.
  
  # If the elemts are not equal, move the pointer by 1 unit.
def removeDuplicates(nums):
        p1 = 0
        p2 = 1
        l = len(nums)
        while p2 < l:
            if nums[p1] == nums[p2]:
                nums.remove(nums[p2])
                l = l - 1
            else:
                p1 = p1 + 1
                p2 = p2 + 1
        return len(nums)
