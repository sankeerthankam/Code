# Approach 1:
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

# Approach 2:
# Check for underlying patterns 
# And implement the pattern
def countBits(nums):
  stem = [0]
  while len(stem) < num+1:
      stem.extend([s + 1 for s in stem])
  return stem[:num+1]
