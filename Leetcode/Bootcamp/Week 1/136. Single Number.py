# In a list of numbers, only one number has a single occurance and the rest occur twice.

# Approach 1:
# Use counter object to count the occurances of each element
# Sort the counter object using .most_common()
# Return the element from the last

# Approach 2:
# Extract the unique elements from the list using the set()
# Twice the sum of the set
# Subtract the sum of the nums from sum of the set

# Approach 3:
# XOR Operation works similarly for bits as well as integers
# a ^ a = 0
# a ^ b = 1
# XOR of two similar elemets is 0 
# XOR of two different elemets is 1
# We do the same to the given list of elements -> It cancels out the similar elements and return the unique one

# Approach 4:
# Sort the numbers
# Assign +, - sign consecutively 
# Sum the list and return the modulus of the result i.e. |res|

def singleNumber(nums):
    from collections import Counter
    c1 = Counter(nums)
    return [i for i in c1.most_common()[-1]][0]

def sol2(nums):
    return 2*sum(set(nums)) - sum(nums)

def sol3(nums):
    # https://www.youtube.com/watch?v=vQbrPU4hW3c
    res = 0
    for i in nums:
        res = res ^ i
    return res
