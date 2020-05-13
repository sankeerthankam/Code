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


# Approach 2:
# Idea here is to move all relevant numbers to the beginning of the array.
# Use a pointer (p1) to keep track of the next available index
# For each i compare elements i-1 and i+1.
  # If they are not equal (i.e. the occurances is less than 3)
  # Move the ith element to p1-th position.
  # Increment the pointer p1.

# At the end of the loop, we have sorted all elements except for the last.
# At this point, assign the last element to p1-th position and increment the pointer (p1)
# Return p1 (i.e. length of the array with duplicate values less than 2)

def removeDuplicates(nums):
  l = len(nums)
  if l < 3:
      return l

  p1 = 1
  for i in range(1, l-1):
      if nums[i-1] != nums [i+1]:
          nums[p1] = nums[i]
          p1 = p1 + 1

  nums[p1] = nums[-1]
  p1 = p1+1
  return p1



# Approach 3:
# White board this

def removeDuplicates(nums):
  i = 0
  for n in nums:
      if i < 2 or n > nums[i-2]:
          nums[i] = n
          i += 1
  return i
