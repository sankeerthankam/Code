# Approach 1:
# Use counter to count the occurances
# RTeturn the least common key

def singleNumber(self, nums: List[int]) -> int:
    from collections import Counter
    c1 = Counter(nums)
    return [i for i in c1.most_common()[-1]][0]

# Approach 2:
# The reason we subtract the result by 2 is becuase all the digits occur thrice and one of them occurs only once (so the diffrence should be divided by 2 to get the digit)
def singleNumber(self, nums: List[int]) -> int:
  return (3*sum(list(set(A)))-sum(A))/2
