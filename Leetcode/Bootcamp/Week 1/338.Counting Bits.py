# For i in range of nums, 
  # Convert i to binary format
  # Convert the binary format to string
  # Count occurances of 1 in the string
  # Append the result to ls

def countBits(nums):
    ls = []
    for i in range(nums+1):
        ls.append(str(bin(i)).count('1'))
        
    return ls
