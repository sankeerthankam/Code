# Approach 1:
# While the loop is sorted
  # Create two pointers 
    # Swap numbers between the two pointers
# Limitation: Time Exceeded

def sortColors(nums):
    while nums != sorted(nums):
         p1 = 0
         p2 = 1
         for i in nums:
             if nums[p1] > nums[p2]:
                 nums[p1], nums[p2] = nums[p2], nums[p1]
                 p1 = p1 + 1
                 p2 = p2 + 1
     return nums

# Approach 2:
# Count the occurances of 0, 1, 2
# Update the list using list comprehension
# Limitation: Not advisable

def sortColors(nums):
    c1 = nums.count(0)
    c2 = nums.count(1)
    c3 = nums.count(2)

    nums[:c1] = [0] * c1
    nums[c1:c1+c2] = [1] * c2
    nums[c1+c2:] = [2] * c3

# Approach 3:
# Create 3 pointers (left, right and zero)
# While the left <= right
    # if left = 0:
      # swap left and zero
      # increment left and zero
    # if left = 2 
      # swap left and right
      # decrement right
    # else (if left = 1)
      # increment left pointer
def sortColors(nums):
    left = 0
    right = len(nums) - 1
    zero = 0
    while left <= right:
        if nums[left] == 0:
            nums[left], nums[zero] = nums[zero], nums[left]
            left += 1
            zero += 1
        elif nums[left] == 2:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1
    # return nums

# Note: You might wonder why you'd need a zero pointer when you can do it with left and right pointers.
# Note: You might alos wonder why you'd need to swap a zero pointer with left pointer.

# Reason: What if you have the input [2, 0, 1]
# At the end of first iteration, your loop would be [1, 0, 2]
# left = 1, right = 2 and zero = 0
# In the second iteration:
  # nums[left] = 0 and nums[right] = 2
  # SInce this is in order, your program outpues [1, 0, 2]
  # This is incorrect
  
# If you have a third pointer and a swap between left and zero pointer
  # After the second iteration, 
    # nums[left] = 0 
    # nums[zero] = 1
    # nums[right] = 2
  # This time, since nums[left] - points to 1, our program swaps - 0 with 1 (i.e. - nums[left] ans nums[zero] would be swapped)
  # At the end of third iteration, you'd have [0, 1, 2]
