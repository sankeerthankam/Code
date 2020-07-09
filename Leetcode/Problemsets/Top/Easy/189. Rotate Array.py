def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    print(k)
    nums[:] = nums[-k:]+nums[:-k]
    
# https://leetcode.com/problems/rotate-array/discuss/54604/Python-Solution-question-Incorrect-answer-on-the-site-but-correct-answer-in-Python-Shell
