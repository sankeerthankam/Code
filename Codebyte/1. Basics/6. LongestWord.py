#  For this challenge you will be determining the largest word in a string.

# Approach: 
# 1. Strip of the leading and trailing spaces
# 2. Substitute special characters with a ','
# 3. Create a '' string and compare its length with the lengths of each word of the string.

import re

def LongestWord(sen): 
  
    sen = sen.strip()
    cleaned_sen = re.sub('[^A-Za-z]+', ',', sen)
    cleaned_sen_list = cleaned_sen.split(',')
    
    word = ''
    for i in cleaned_sen_list:
      if len(i) > len(word):
        word = i
      elif len(i) == len(word):
        pass
    # code goes here 
    return word
    
# keep this function call here  
print(LongestWord(input()))
