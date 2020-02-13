# Convert the binary input to a 32 digit bin string ['{0:032b}'.format(n)]
# i.e. If there is a number that has 16 digits, the below operation ensures that 0s are added to the leading digits are 
# Ex: '1100' will become '00000000000000000000000000001100'
# Reverse the string  
# Convert it to int with base 2

def reverseBITS(n):
    n = '{0:032b}'.format(n)
    n = n[::-1]
    return int(n,2)
