# Approach 1
# For each element, extract the max of the rest using slicing

def replaceElements(self, arr: List[int]) -> List[int]:
  for i in range(len(arr)-1):
      arr[i] = max(arr[i+1:])
  arr[-1] = -1
  return arr


# Approach 2
# Starting at the end of the array, at each position there are three things to do:
# 1. Hold the value in that position
# 2. Insert maximum number until that position
# 3. Compare 'hold' value with maximum value, the greater is new maximum number.

#    First maximum number value is -1.
#    First 'hold' value is value at the end of array

def replaceElements(self, arr: List[int]) -> List[int]:
  maxNum = -1
  for i in range(len(arr)-1,-1,-1):
      hold = arr[i]
      arr[i] = maxNum
      if hold > maxNum:
          maxNum = hold
  return arr
