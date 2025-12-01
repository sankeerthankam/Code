# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Note that the product of an array with a single element is the value of that element.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

def maxProduct(self, nums: List[int]) -> int:
    res = max(nums)
    curr_max = 1
    curr_min = 1
    for n in nums:
        temp = curr_max*n 
        curr_max = max(n, temp, curr_min*n)
        curr_min = min(n, temp, curr_min*n)
        res = max(res, curr_max)
    return res

# Complexity Analysis
# Time Complexity: O(n) - We iterate through the array once, making constant-time calculations at each step.
# Space Complexity: O(1) - Only a few variables are used for tracking the state.
