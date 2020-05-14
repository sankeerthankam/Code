def duplicateZeros(nums):
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    l = len(nums)
    while i < l:
        if nums[i] == 0:
            nums[i:i] = [0] # Add another 0 at the occurance of 0
            del nums[-1]    # Delete last element in the array
            i = i + 1       # Increment i twice
        i = i + 1
    # return nums
