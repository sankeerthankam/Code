# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(self, nums: List[int]) -> bool:
    num_set = set()
    for n in nums:
        if n in num_set:
            return True
        else:
            num_set.add(n)
    return False

# Time Complexity: O(n), As we are traversing over the array once.
# Auxiliary space: O(n), As we are using unordered set which takes O(n) space in worst case, where n is the size of the array.

def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i]==nums[i-1]:
            return True
    return False

# Time Complexity: O(n * logn), As we are using sorting function which takes nlogn time.
# Auxiliary space: O(1), As we are not using extra space.

