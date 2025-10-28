def twoSum(self, nums: List[int], target: int) -> List[int]:
    lookup_map = {}
    for i, j in enumerate(nums):
        lookup_val = target - j
        if lookup_val in lookup_map:
            return [lookup_map[lookup_val], i]
        else:
            lookup_map[lookup_val] = i
