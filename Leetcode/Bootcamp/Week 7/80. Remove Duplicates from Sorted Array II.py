# Approach 1:
# Naïve approach: # Same as 80. Remove Duplicates from Sorted Array I
# Use two pointers p1, p2 and a cnt variable to count the number of occurances,
# If the number of occurances > 2, 
  # remove the element
  # shorten the length (since you have deleted the element)
  # reduce the count (since you have deleted the element)
  # **Do not increment the pointers**


def removeDuplicates(nums):
  p1 = 0
  p2 = 1
  cnt = 1
  l = len(nums)
  while p2 < l:
      if nums[p1] == nums[p2]:
          cnt += 1

          if cnt > 2:
              nums.remove(nums[p2])
              l = l-1
              cnt -= 1
          else:    
              p1 += 1
              p2 += 1

      else:
          p1 += 1
          p2 += 1
          cnt = 1
  return nums
