# Naive Approach
# This approach does not work for edge cases 
def maxSubArrayLen(nums, k):
  max_so_far = 0
  for i in range(len(nums)):
      for j in range(i, len(nums)):
          if sum(nums[i:j]) == k:
              max_so_far = max(max_so_far, len(nums[i:j]))
  if max_so_far:
      return max_so_far
  else:
      return 0
