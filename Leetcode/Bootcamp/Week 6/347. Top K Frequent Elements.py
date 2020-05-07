def topKFrequent(nums, k):

  if len(nums) == 1 and k == 1:
      return nums

  from collections import Counter
  return [i[0] for i in Counter(nums).most_common(k)]
