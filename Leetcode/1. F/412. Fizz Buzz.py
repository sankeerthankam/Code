# 412. Fizz Buzz
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.


# Approach
# If element is divisible by 3 and 5 -> FizzBuzz
# Else:
  # If element is divisble by 3 -> Fizz
  # If element is divisble by 5 -> Buzz
  # Else: Append -> str(i)
  
# Note: Pay special attention to the order in which the if, elif and else statements are written

def fizzBuzz(self, n: int) -> List[str]:
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('FizzBuzz')    
        elif i % 3 == 0 :
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res
