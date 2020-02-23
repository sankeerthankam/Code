# Approach 1:
# Write a function that return the sum of digits of a number
# While the sum is not in the range (0-9)
  # Continue calculating the sum of digits
  # Update the sum_ with new sum_
# Reutrn the sum_

# Approach 2:
# This problem follows a pattern
# Its the quotient of num % 9

def addDigits(num):
    
    def sum_of_digits(n):
        return sum([int(i) for i in str(n)])
    
    sum_ = sum_of_digits(num)
    
    if sum_ in range(0, 10):
        return sum_

    else:
        while sum_ not in range(0, 10):
            sum_ = sum_of_digits(sum_)
        return sum_
        
def addDigits(num):
    return num % 9
