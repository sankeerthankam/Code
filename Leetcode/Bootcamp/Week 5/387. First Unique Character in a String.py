# Approach 1:
# For each char in the string, traverse therough the string again to check its second occurance
# This hass O(N^2) time-complexity
def firstUniqChar(s):
    l = len(s)
    for i in range(l):
        ch = s[i]
        if ch not in s[:i]+s[i+1:]:
            return i
    return -1

# Approach 2:
# User counter from itertools (COunter preserves the order)
def firstUniqChar(s):
    for i,j in Counter(s).items(): 
        if j == 1: return(s.index(i))
    return -1
