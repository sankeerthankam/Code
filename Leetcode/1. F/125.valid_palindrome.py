class Solution:
    def isPalindrome(self, string: str) -> bool:
        string = string.lower()
        string = re.sub('[^a-z0-9]', '', string)
        if string == string[::-1]:
            return True
        else:
            return False
