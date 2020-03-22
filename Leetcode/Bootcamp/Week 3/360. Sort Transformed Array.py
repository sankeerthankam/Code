def sortTransformedArray(nums, a, b, c):
    ls = []
    for i in nums:
        ls.append(a*(i**2) + b*(i) + c)
    return sorted(ls)
