def removeDuplicates(nums):
  l = 1
  for i in range(len(nums)-1):
      if nums[i] != nums[i+1]:
          nums[l] = nums[i+1]
          l = l + 1
  return l
  
  # https://github.com/sankeerthankam/Code/blob/master/Leetcode/Learn/1.%20Array/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py
