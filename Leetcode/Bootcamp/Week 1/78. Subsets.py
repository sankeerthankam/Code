# Import combinations from itertools
# for the range of length of the array
# Create combinations from the set for  (1, 2 ... len(array) 
  # [1], [2], [3]
  # [1, 2], [1, 3], [2, 3]
  # [1, 2, 3]
# Append the result and return the result

def subsets(nums):
    from itertools import combinations
    ls = []
    for i in range(len(nums)+1):
        for i in combinations(nums, i):
            ls.append(list(i))
    return ls
