def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Left pointer and Right pointer starts at 0
    Right increments by 1 in the for loop
    When right pointer encounters a non-zero element, we swap the right element with the left element
        And incerement left pointer by 1 (since it has already been updated)
    """
    l = 0 
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l = l + 1
    return nums
