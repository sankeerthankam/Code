# Approach 1
# https://www.youtube.com/watch?v=cFd4-Dz8l4g

def threeSum(nums):
  nums = sorted(nums)
  result = set()
  for i in range(len(nums)):
      l = i + 1
      r = len(nums) - 1
      target = 0 - nums[i]
      while l < r:
          if nums[l] + nums[r] == target:
              result.add((nums[i], nums[l], nums[r]))
              l += 1
              r -= 1
          elif nums[l] + nums[r] < target:
              l += 1
          else:
              r -= 1
  return list(result)
    
# Approach 2
# Extension of TwoSUm problem 

def threeSum(nums):
  def twoSum(nums,target,ans):
      d = {}
      for i,v in enumerate(nums):
          if target-v in d:
              ans.add((v,target-v,-target)) #3sum wants the numbers, while 2sum wanted the indices
          d[v] = i

  nums.sort()
  ans = set()
  for i,v in enumerate(nums):
      twoSum(nums[i+1:],-v,ans)
  return ans
