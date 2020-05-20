# Approach 1:
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

# Approach 2
# The following is faster but uses extra space though
def removeDuplicates(nums):
  nums[:] = sorted(set(nums))
  return len(nums)

# Approach 3
def removeDuplicates(nums):
  x = 1
  for i in range(len(nums)-1):
      if(nums[i]!=nums[i+1]):
          nums[x] = nums[i+1]
          x+=1
  return(x)
