# Approach 1:
# Divide the divided by divisor until dividend is less than or equal to divisor
# Increment quotient for each iteration

# Note:
# You can traverse through half the length of the divided and multiply the quotient to get the result
# But that requires us to use * and / which is prohibited by the leetcode question

def div(dividend, divisor):
    q = 0
    while dividend >= divisor:
        dividend = dividend - divisor
        q = q + 1
    return q
    
# Approach 2:
# Idhi explain cheyatam kashtam.
# Commentlu chadhuvu ko ra nayana !

def div(dividend, divisor):
    is_negative = (dividend < 0) != (divisor < 0)
    divisor, dividend = abs(divisor), abs(dividend)

    quotient = 0
    the_sum = divisor

    while the_sum <= dividend:
        current_quotient = 1
        
        # Inner loop increments quotient at the rate of (1, 2, 4, 8, 16 etc.)
        # Once the threshold is reached (half of the dividend), loop breaks
        # For each iteration, we double the quotient and the_sum
        while (the_sum + the_sum) <= dividend:
            the_sum = the_sum + the_sum
            current_quotient = current_quotient + current_quotient
        
        # Now that we came out of the inner loop, we subtract out dividend by the 'the_sum'
        # This is to update the quotient only after half way
        # For each iteration, we decrement the dividend by (dividend - the_sum) 
        # and increment the quotient by 1
        dividend = dividend - the_sum
        the_sum = divisor
        quotient = quotient + current_quotient

    return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))
