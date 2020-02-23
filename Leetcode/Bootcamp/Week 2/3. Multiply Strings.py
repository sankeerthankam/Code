# Approach 1: 
# Type Cast number to integer
# Multiply the numbers
# Type cast it back to string and return the result

def multiply(num1, num2):
    return str(int(num1)*int(num2))
    
# Approach 2  
# Assign n1, n2 = 0
# Traverse through each character in each string and convert the character to int using ord(i) - ord('0')
# Multiply the two numbers (which are currently in 'int')
# Reverse the product (integer) and append the result char by char
    # For each digit from the last (extract the remainder)
    # Append the digit to the result as a string using (chr(ord('0) + digit))
# Now that you have a product as string, reverse the string and return the result

def multiply(num1, num2):
    
    if num1 == "0" or num2 == "0":
        return "0"
        
    n1, n2 = 0, 0

    for i in num1:
        n1 = n1*10 + (ord(i) - ord('0'))
    for j in num2:
        n2 = n2*10 + (ord(j) - ord('0'))

    prod = n1*n2
    res = ''

    while prod:
        dig = prod % 10
        res = res + chr(ord('0') + dig)
        prod = prod // 10

    return res[::-1]
