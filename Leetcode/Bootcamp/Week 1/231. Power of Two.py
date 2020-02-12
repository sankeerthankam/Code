# One problem I ran into with this approach is that the machine's inaccurate storage of floating-point 
# values led to erroneous results for large values of n, so I rounded the result out to 11 decimal places

def isPowerOfTwo(n):
    if n <= 0:
        return False
    import math
    return round(math.log(n, 2), 11).is_integer()
    
# If a number is a power of two - then it should have only single occurance of 1 in its binary representation

def isPowerOfTwo(n):
    return (n > 0 and bin(n).count('1') == 1)
