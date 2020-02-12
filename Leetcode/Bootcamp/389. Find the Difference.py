# Set comparision would not be useful because set does not take duplicate characters into consideration.
# i.e. 'aa' is the same as 'a'
# Use Couter object here to get the count of each character in each word
# Couter differences is the same as set differences
# Return the key in the difference of the two counter objects

def findTheDifference(s, t):
    c1 = Counter([i for i in s])
    c2 = Counter([i for i in t])

    return ''.join([i[0] for i in c2 - c1])
