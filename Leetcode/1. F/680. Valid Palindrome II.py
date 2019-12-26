class Solution:
    import re
    def isPalindrome(string):
        string = string.lower()
        string = re.sub('[^a-z0-9]', '', string)
        if string == string[::-1]:
            return True
        else:
            return False

    def validPalindrome(self, ss: str) -> bool:
        i = 0
        j = len(ss)-1
        while (i <= j and ss[i] == ss[j]): 
            i = i + 1
            j = j - 1
        if i > j: 
            return True

        return isPalindrome(ss[i:j]) or isPalindrome(ss[i+1:j+1])
