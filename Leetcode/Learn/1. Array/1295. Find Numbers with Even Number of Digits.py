# Approach 1
# Type convert int to str, Calculate len of each string and store them in list comp
# Return len of list

def findNumbers(nums):
    x = map(lambda x: len(str(x)), nums)
    return len([i for i in x if i%2 == 0])
    
# Approach 2:
# Naïve Approach
    
def findNumbers(nums):    
  cnt = 0
  for i in nums:
      if len(str(i)) %2 == 0:
          cnt += 1
  return cnt
