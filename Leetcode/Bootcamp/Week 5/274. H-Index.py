"""
H-Index: Sort the array in a descending order
For every element, check if its less than its index 
    If not - return the most recent index
"""


# Approach 1
# Edge cases:
  # If empty array -> return 0
  # If array has single element 
    -> return 1 if ele > 0 
    -> else return 0
# Sort the array and enumerate to keep track of the index
# Note that the index in enumerate starts at 0 -> So, we have to compare the list value with i+1
# When list value is < index, return the most recent index
# Finally, if all the elements in the list sucessfully satisfy the criteria of H-Index, then return i+1

def hIndex(citations):
    # Edge cases
    if len(citations) < 2:
        if len(citations) == 1 :
            if citations[0] > 0:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        for i, j in enumerate(sorted(citations, reverse = True)):
            if i+1 <= j:
                continue
            else:
                return i 

        # If all the elements in the sorted array are greater than its index value, then return i+1 (since enumerated index starts at 0)
        return i + 1
