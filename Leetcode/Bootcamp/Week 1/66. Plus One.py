# Convert the list of numbers to string
# Combine each string i.e. '1', '2', '3' becomes '123'
# Type cast the string to int and add 1 to it
# Type cast the result from above to string
# Using list comprehension convert the digits to int and return the result

def plusOne(digits):
    return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]
