# For this challenge you will be determining the factorial for a given number.

def FirstFactorial(num): 

    fact = 1
    for i in range(num):
      fact = fact * (i +1)
    return fact
    
print(FirstFactorial(input()))
