# Approach 1:
# Convert the integer to binary and then into string
# Return the count of 1s

def hammingWeight(n):
    return str(bin(n)).count('1')

# Approach 2:
# https://www.youtube.com/watch?v=KJnhAUkxAho
# Use bit manipulation as shown in the above video
def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
