# Approach 1
# Use two variables current_sum and max_sum
# current_sum denotes the running sum as you loop through the array while max_sum denotes the max_sum you have encountered so far

# How current_sum is populated:
  # Initialize current_sum = 0
  # Since we have to calculate the running total, as you travserse through the list, keep adding the element (i) to the sum.
  # However, there's a catch here. Sometimes you might come across a situation where element (i) > running total so far.
  # [-2, -3, 3, 2, 6, 1]
  # Here at element 6, the current_sum is 0 while i = 6.
  # So, the following code snippit fixes such edge case.
  # current_sum = max(current_sum + i, i)

# How max_sum is updated
  # Once the current_sum is populated, update max_sum when current_sum ? max_sum


def maxSubArray(nums):
    current_sum = 0
    max_sum = float('-inf') 
    for i in nums:
        current_sum = max(current_sum + i, i)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
