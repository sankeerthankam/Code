# Assign negative = False to keep track of the sign of the integer
# If input (x) is a negative num, make the 'negative' variable = True and update the num to positive (x = -x)
# While the temp number is not 0, 
    # Extarct each digit 
    # Add it to the reverse integer (rev * 10) + digit
    # Update the input (x)
# If the number is out of range, return 0
# Else update the reversed number with its respective (+ve or -ve sign) adn return the result

def reverse(x):

    negative = False

    if x < 0:
        negative = True
        x = -x

    rev = 0
    while x:
        # dig = temp % 10
        rev = rev * 10 + (x % 10)
        x = x // 10

    if rev > pow(2, 31):
        return 0
    else:
        return rev*-1 if negative else rev
