# Approach:
# let x = 8
# [0 1 2 3 4 5 6 7 8]
# left = 0
# right = 8
# mid = 4
# Since 4**2 (16) > 8
  # we update right = 3 (4-1) i.e. mid - 1

# Peform binary search until you find the right element

def sqrt(x):
    
    left = 0
    right = x

    while left <= right:
        # // performs floor division i.e floor(a/b)
        mid = (left + right)//2
        if mid**2 > x:
            right = mid - 1a
        elif mid**2 < x:
            left = mid + 1
        else:
            return mid

    # Note: Since we are rounding down, we return right
    # If we were to round up, we would be returning left.
    
    return right
