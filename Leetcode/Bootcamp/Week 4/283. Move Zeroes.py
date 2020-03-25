# Approach 1
# Smart but not advisable
nums.sort(key=bool, reverse=True)

# Approach 2
# Two pointer - left and right
# If left == 0: pop and append at the end - decrement right
# Else: increment left 

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    zero = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == 0:
            nums.pop(left)
            nums.append(0)
            right -= 1
        else:
            left += 1

# Approach 3
# Swap every element if it's not 0
# Not the best solution. What about when all nums are non zeroes? In that case you are stil swaping the variable with itself
def moveZeroes(self, nums):
  zero = 0  # records the position of "0"
  for i in xrange(len(nums)):
      if nums[i] != 0:
          nums[i], nums[zero] = nums[zero], nums[i]
          zero += 1
