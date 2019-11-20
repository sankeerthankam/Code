# 238. Product of Array Except Self
# Split the array into left_sub_array and right_sub_array and multiply their products

import numpy as np
def productExceptSelf(arr):
    ls = []
    for i in range(len(arr)):
        left_arr = arr[:i]
        right_arr = arr[i+1:]
        # left_prod = prod(left_arr)
        # right_prod = prod(right_arr)
        prod = np.prod(left_arr) * np.prod(right_arr)  
        ls.append(int(prod))
    return ls
    
    
def prod(arr):
    prod = 1
    for i in arr:
        prod = prod * i
    return prod
