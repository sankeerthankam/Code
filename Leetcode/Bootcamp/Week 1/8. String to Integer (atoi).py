# Strip the leading spaces
# If string is empty, return 0
# Check if the first character of the string is + or -
  # Extract the sign 
  # Extract the number
# For each char in the string:
  # If its a digit -> assign it to result string (num)
  # Else break 

# Use exception handling for the following code:
  # Once you have extracted the number -> type cast it to int
  # If the int(value) is a overflow i.e. (> pow(2, 32) or < pow(2, 32)) -> return the max_int
  # Else return value
# If an exception has been encountered -> return 0

def myAtoi(str):
    
    num = ''
    #remove left spaces
    str = str.lstrip(' ')

    # check empty string
    if (not str):
        return 0

    # check minus/plus signs
    if (str[0] == '-' or str[0] == '+'):
        num = str[0]
        str = str[1:]

    # check digits
    for ch in str:
        if (ch.isdigit()):
            num = num + ch
        else:
            break

    try: 
        value = int(num)
        #check overflow
        if (value.bit_length() >= 32):
            return (2**31-1) if value > 0 else -2**31
        return value
    
    except ValueError:
        return 0
