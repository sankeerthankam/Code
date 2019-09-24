# For this challenge you will be capitalizing certain characters in a string.

def LetterCapitalize(str): 

    # return str.title()
    return ' '.join([s[0].upper() + s[1:] for s in str.split()])
     
print(LetterCapitalize(input()))

# Comments: 
# Approach 1: str.title() - Capitalizes every letter after a special character as well as spaces.
# Approach 2: convert to list and capitalize - Capitalizes only letter after spaces.
