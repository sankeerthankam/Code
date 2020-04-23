# White board the solution to understand it better.
# Took me 3 partial days to get to this solution
def increasingTriplet(nums):
    
    count = 0
    max1 = float('inf')
    max2 = float('inf')

    # Checks if a < b < c
    for i in nums:
        if i <= max1:
            max1 = i
        elif i <= max2:
            max2 = i
        else:
            return True
    return False
