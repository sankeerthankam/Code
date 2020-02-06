# Check if the number is +ve or -ve
# If negative update the number to be positive 
# Reverse the number using "digit extraction technique"
# Return the result:
# - If the given number is negative, return result * -1
# - Else return result
# Corner case: If the result in pow(2, 31) return 0


def reverse(self, x: int) -> int:

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
