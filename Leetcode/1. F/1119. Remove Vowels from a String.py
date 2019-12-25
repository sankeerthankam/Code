# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# Approach 1
# Traverse through each letter 
# Check if they belong to vowels 
# Use list comprehensions to exclude vowels
# Join the list to form a string

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        str_without_vowels = ''.join([i for i in S if i not in vowels])
        return str_without_vowels
