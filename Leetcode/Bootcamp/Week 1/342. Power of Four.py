def isPowerOfFour(num):
    if num <= 0:
        return False
    
    return round(math.log(num, 4), 11).is_integer()
