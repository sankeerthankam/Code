# Convert the integer to binary and then into string
# Return the count of 1s

def hammingWeight(n):
    return str(bin(n)).count('1')
