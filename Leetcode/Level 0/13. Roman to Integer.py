# Rever the string
# Initialize prev = 0
# Traverse through each character
  # Check if the current char >= prev - If so add the number to the list
  # Else add number * -1 to the list
# Return the sum

def roman_to_int(nums):
    lookup = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    ls = []
    
    prev = 0
    for i in nums[::-1]:
        if lookup.get(i) >= prev:
            ls.append(lookup.get(i))
        else:
            ls.append(lookup.get(i) * -1)
        prev = lookup.get(i)
    return sum(ls), ls
