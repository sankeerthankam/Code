# Approach 1:
# The following is faster but uses extra space though

def removeDuplicates(nums):
  nums[:] = sorted(set(nums)) # nums[:] represents all elements in the list i.e. here it is used to assign result to all values in `nums`
  return len(nums)


# Approach 2:
# Use two pointer p1 and p2
# While p2 < len(nums)
  # Compare two elements next to each other and remove if they are equal.
  # Once you remove the element in place, the size of the array also decreases, hence update l = l - 1 
  # Do not increment the pointers here, since you have already deleted the element in place.
  
  # If the elemts are not equal, move the pointer by 1 unit.
def removeDuplicates(nums):
    p1 = 0
    p2 = 1
    l = len(nums)
    while p2 < l:
        if nums[p1] == nums[p2]:
            nums.remove(nums[p2])
            l = l - 1
        else:
            p1 = p1 + 1
            p2 = p2 + 1
    return len(nums)

# Approach 3:
# The following approach only return the length of the unique elements. It does not modify array in place.
# Use a pointer p1 and initialize it to 1. 
# While traversing through the loop, compare two elements (i, i+1)
  # If they are equal, continue traversing to find the next unique element.
  # When you find the unique element, replace 
  #     Since, our first element is already present at index 0 (it is a unique element), we quickly run a for loop for the entire array to scan for unique elements.
  #     If the current element and the next element are the same, then we just keep on going till we find a different element
  #     Once we find a different element, it is inserted at index 1, because, index 0 is taken by the first unique element.
  #     Once this is done, the same scanning is done to find out the next unique element and this element is to be inserted at index 2. This process continues until we are done with unique elements.
  #     We use a variable (x = 1) which is incremented to the next index whenever we find a unique element and we insert this element at its corresponding index.


def removeDuplicates(nums):
    p1 = 1
    for i in range(len(nums)-1):
        # If two adjacent elements are not equal, assign the pointer with i+1
        # Increment the pointer
        if(nums[i]!=nums[i+1]):
            nums[p1] = nums[i+1]
            p1 = p1 + 1
    return(x)
