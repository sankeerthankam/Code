# Approach:
# While n != 1
  # If the number is divisible by 2, continue dividing it by 2
  # Else If number is 1 more than a multiple of 4 (i.e. number %4  == 1) or number = 3
    # then subtract 1 from the number (n = n-1)
  # Else (i.e., the number is not a multiple of 2, the number is not 1 more than multiple of 4 -- so, the number must be 3 more than multiple of 4; n%4 == 3)
    # then add 1 tp the number
  # for each of the above operation, add 1 to the count.'
  
  
def integerReplacement(n):

    count = 0

    while n != 1:
        if n % 2 == 0:
            n = n //2



        elif n % 4 == 1 or n == 3:
            n -= 1
        else:
            n += 1
        count += 1
    return count
    
    
# https://leetcode.com/problems/integer-replacement/discuss/502367/python-100-(8ms)-easy-to-read-a-simple-logic-in-one-while-loop-explained
# https://leetcode.com/problems/integer-replacement/discuss/407631/Python-Simple-Solution
