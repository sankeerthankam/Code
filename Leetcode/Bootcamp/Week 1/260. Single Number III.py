# Approach 1:
# Use counter object
def singleNumber(nums):
    from collections import Counter
    c1 = Counter(nums)
    return [i[0] for i in c1.most_common()[-2:]]


# Approach 2:
# Naive Solution
# Keep track of num of occurances of each element

def singleNumber(nums):
    one = set()
    double = set()
    for n in nums:
        if n not in one:
            one.add(n)
        else:
            double.add(n)

    return list(one - double)


# Approach 3:
# Naive Solution (Improved)
# Keep track of num of occurances of each element

def singleNumber(nums):
    res = set()
    for i in nums:
        if i not in res:
            res.add(i)
        else:
            res.remove(i)

    return list(res)
