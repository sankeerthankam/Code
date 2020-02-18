def singleNumber(self, nums: List[int]) -> int:
    from collections import Counter
    c1 = Counter(nums)
    return [i for i in c1.most_common()[-1]][0]

def singleNumber(self, nums: List[int]) -> int:
  return (3*sum(list(set(A)))-sum(A))/2
