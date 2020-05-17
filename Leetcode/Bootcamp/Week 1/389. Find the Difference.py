# Approach 1:
# Set comparision would not be useful because set does not take duplicate characters into consideration.
# i.e. 'aa' is the same as 'a'
# Use Couter object here to get the count of each character in each word
# Couter differences is the same as set differences
# Return the key in the difference of the two counter objects

def findTheDifference(s, t):
    c1 = Counter([i for i in s])
    c2 = Counter([i for i in t])

    return ''.join([i[0] for i in c2 - c1])

# Approach 2:
# Sort the strings -> This returns a list
# Since the first string is 1 letter short of second string, add [''] to the first sorted list
# Zip two lists and compare each elements
# When there is a mismatch, return the char from the second list

def findTheDifference(a, b):
    for i, j in zip(sorted(a) + [''], sorted(b)):
        if i != j:
            return j

# Approach 3 
# Sum each char of the two strings and return the char(diff in sum)
def findTheDifference(s, t):
    ssum = sum([ord(i) for i in s])
    tsum = sum([ord(i) for i in t])
    return chr(tsum - ssum)
