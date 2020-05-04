# Approach 1
# Compare each char in secret and guess 
    # If there's a match -> increment b
    # Else: Update the dictionary, if this is the first occurance
# For each element in secret dictionary 's', if it is in 'g', update a = min(s[k], g[k])
    
# Instead of throwing a 'Key-Value' error, this code snippet will return 0, if there is no value found.
# s.get(secret[i], 0)

# Instead of returning 0 as explained in the above code snippet, this will return 1
# s.get(secret[i], 0) + 1
  
# This is update or create a record in the dictionary.
# s[secret[i]] = s.get(secret[i], 0) + 1

def getHint(secret, guess):

    bull, cow = 0, 0
    secret_dict = {}
    guess_dict = {}
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull = bull + 1
        else:
            secret_dict[secret[i]] = secret_dict.get(secret[i], 0) + 1
            guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1
            
            
    for ele in secret_dict:
        if ele in guess_dict:
            cow += min(secret_dict[ele], guess_dict[ele])
        
    return '{0}A{1}B'.format(bull, cow)
