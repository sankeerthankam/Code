# Approach 1:
# COnvert the sentence to lower case and strip the trailing and leading spaces
# Using regex, replace special characters with empty string

def isPalindrome(s):
  s = s.strip().lower()
  import re
  s = re.sub('[^a-z0-9]+', '', s)
  return s[::-1] == s
