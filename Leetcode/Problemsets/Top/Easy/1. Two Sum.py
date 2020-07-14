def twoSum(nums, target):
  ls = []
  dict_ = {}
  for ind, ele in enumerate(nums):
      if target - ele in dict_:
          ls.append(ind)
          ls.append(dict_[target - ele])
          return ls
      else:
          dict_[ele] = ind
