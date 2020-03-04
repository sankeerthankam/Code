def trailingZeroes(n):
    # https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52510/O(log5_n)-solution-python.
    # Drivide the number with 5 until n!= 0
        # Add the quotients (floor quotient)
    # Return the sum

    if n < 5:
        return 0

    r = 0
    while n != 0:
        n //= 5
        r += n
    return r
