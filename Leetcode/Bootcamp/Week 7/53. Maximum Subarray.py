# Approach 1: 
# Since we are to return only sum, we do not use pointers.
# Initialize variable max_sum, current_sum with value of first element
# As you traverse through 
  # Update current_sum as max(arr[i], current_sum+arr[i]) -> This is because if the current ele is greater than sum so far, ONLY then we update the current sum
  # max_sum is max(max_sum, curren_sum)
# Return max_sum

def maxSubArray(arr):
  l = len(arr)
  max_sum = arr[0]
  current_sum = arr[0]

  if l == 1:
      return max_sum

  for i in range(1, l):
      current_sum = max(arr[i], current_sum+arr[i])
      max_sum = max(max_sum, current_sum)
  return max_sum
