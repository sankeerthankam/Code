# Traverse through each element in the list
# While traversing through each element, calculate the 'complement/required' number
# Create a list of visited_elements
# For example: target_sum = 9, nums = [2, 7, 11, 15]; 
# Here i = 2, required/complement = 7 -> So, we look for 7 in the rest of the list
# When required element is found, return the indices from visited_list
# Note: Might work only on a sorted list

def twoSum(self, nums: List[int], target: int) -> List[int]:
    visited_elements = {}
    for i in range(len(nums)):
        required = target - nums[i]
        if required not in visited_elements:
            # add current element to visited elements
            visited_elements[nums[i]] = i
        else:
            # returns index of the visited element and current element
            return visited_elements[required], i
