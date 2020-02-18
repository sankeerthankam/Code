def singleNumber(nums):
    from collections import Counter
    c1 = Counter(nums)
    return [i[0] for i in c1.most_common()[-2:]]
