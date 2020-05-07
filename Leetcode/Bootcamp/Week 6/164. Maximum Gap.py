def maximumGap(nums):

    if len(nums) < 2:
        return 0

    else:
        max_ = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] > max_:
                max_ = nums[i+1] - nums[i]
        return max_
