# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Two pass solution using two Hashmaps
def isAnagram(self, s: str, t: str) -> bool:
    counter_s = {}
    counter_t = {}
    for i in s:
        if i not in counter_s:
            counter_s[i] = 1
        else:
            counter_s[i] = counter_s.get(i) + 1 
    for j in t:
        if j not in counter_t:
            counter_t[j] = 1
        else:
            counter_t[j] = counter_t.get(j) + 1
    if counter_s == counter_t:
        return True
    else:
        return False

# Two pass solution using two Hashmaps

from collections import Counter
def isAnagram(self, s: str, t: str) -> bool:
    # Early return if strings have different lengths
    if len(s) != len(t):
        return False
  
    # Count frequency of each character in string s
    char_count = Counter(s)
  
    # Iterate through string t and decrement character counts
    for char in t:
        char_count[char] -= 1
        # If count goes negative, t has more of this character than s
        if char_count[char] < 0:
            return False
  
    # All characters matched successfully
    return True

# Time & Space Complexity
# Time complexity: 
# O(n+m)
# Space complexity: 
# O(1) since we have at most 26 different characters.
