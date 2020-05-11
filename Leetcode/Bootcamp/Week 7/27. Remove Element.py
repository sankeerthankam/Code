
def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

# Resources: 
# https://stackoverflow.com/questions/7118276/how-to-remove-specific-element-from-an-array-using-python
# https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists/11520540
