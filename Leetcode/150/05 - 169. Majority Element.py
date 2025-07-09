"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement(self, nums: List[int]) -> int:
    count = 0
    majority = 0
    
    # for each element, update the majority variable to 'i' when count is 0
    for i in nums:
        if count == 0:
            majority = i

    # Increment count if variable 'majority' is equal to variable 'i' 
        if i == majority:
            count = count + 1
    
    # Decrement count if variable 'majority' is not equal to variable 'i' 
        else:
            count = count - 1

    return res
