# Use counter object to count the character occurances
# Use most_common() to sort the keys based on values
# Return the last key

def singleNumber(self, nums: List[int]) -> int:
    from collections import Counter
    c1 = Counter(nums)
    return [i for i in c1.most_common()[-1]][0]
