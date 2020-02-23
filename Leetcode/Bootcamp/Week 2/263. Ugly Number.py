 # Approach 1:
 # Calculate prime numbers until n
 # Calculate factors of n
 # Perform the intersection of the two sets to get the prime factors of 'n'
 # Return True if max(prime_factors) > 6 
 
 def isUgly(num):

    if num == 0 or num > pow(2, 31) or num < pow(2, -31):
        return False
    if num == 1:
        return True

    def primes(num):
        import math
        ls = []
        for num in range(2,num+1):
            if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
                ls.append(num)
        return ls

    def factors(num):
        f = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                f.append(i)
                f.append(divmod(num, i)[0])
        return set(f)

    f = factors(num)
    p = primes(num)

    prime_factors = f.intersection(p)

    # If the max of all_primes if greater than 5, then the number is not ugly
    return True if max(prime_factors) < 6 else False


    
# Approach 2:
# Keep dividing the number until its no longer divisible by 5 
# Do the same for 3 and 2

def isUgly(num):
    if num == 0: 
        return False
    while num % 5 == 0: 
        num /= 5
    while num % 3 == 0: 
        num /= 3
    while num % 2 == 0: 
        num /= 2
    return num == 1
