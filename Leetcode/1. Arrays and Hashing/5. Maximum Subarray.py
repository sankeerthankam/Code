# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(self, nums: List[int]) -> int:
    max_sub = nums[0]
    curr_sum = 0
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum = curr_sum + n
        max_sub = max(max_sub, curr_sum)
    return max_sub


# But we can simply optimize that by storing the max at each iteration instead of separately calculating it at the end.
# Thus, we only need to maintain curMax which is the maximum subarray sum ending at i and maxTillNow which is the maximum sum we have seen till now. 
# And this way of solving this problem is what we popularly know as Kadane's Algorithm
# Works with list with all negative numbers 

def maxSubArray(self, nums: List[int]) -> int:
    max_sub = -inf
    curr_sum = 0
    for n in nums:
        curr_sum = max(n, curr_sum + n)
        max_sub = max(max_sub, curr_sum)
    return max_sub

# Time Complexity : O(N), for iterating over nums once
# Space Complexity : O(1), only constant extra space is being used.
