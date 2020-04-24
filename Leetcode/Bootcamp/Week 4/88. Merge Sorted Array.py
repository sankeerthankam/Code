# Compare the last element of the seconf array with the last initialized element of the first array
# White board it to understand it better

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # nums1[:] =  sorted(nums1[:m] + nums2[:n])
    while m >0 and n > 0:
        if nums1[m-1] < nums2[n-1]:
            nums1[m+n-1] = nums2[n-1]
            n = n - 1
        else:
            nums1[m+n-1] = nums1[m-1]
            m = m - 1
    nums1[:n] = nums2[:n]
