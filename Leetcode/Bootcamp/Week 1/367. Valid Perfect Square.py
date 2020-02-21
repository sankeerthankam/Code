# Approach 1:
# Brute Force until half+1

def isPerfectSquare(num):
    if num == 1:
        return True
    for i in range((num//2)+1):
        if i * i == num:
            return True
    return False

# Same logic as Leetcode - 69 sqrt()
def isPerfectSquare(num):
    left = 0
    right = num

    while left <= right:
        # // performs floor division i.e floor(a/b)
        mid = (left + right)//2
        if mid**2 > num:
            right = mid - 1
        elif mid**2 < num:
            left = mid + 1
        if mid**2 == num:
            return True

    # Note: Since we are rounding down, we return right
    # If we were to round up, we would be returning left.
    
    return False
