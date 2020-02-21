# Apprach 1:
# Seieve of Erasthosthanes
# In the inner for loop. we iterate from 2 to n/2
  # For all multiples of i, we update the result with False
  
def countPrimes(n):
    # https://www.youtube.com/watch?v=eKp56OLhoQs
    if n <= 2:
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in range(2, n):
        if res[i] == True:
            for j in range(2, (n-1)//i+1):
                res[i*j] = False
    return sum(res)


# In the inner for loop. we iterate from 2 to sqrt(n)+1
  # Create a sublist (For all multiples of i in the list i.e. result[i*i : n : i])
    # Update the values in the sublist as False
    
  def countPrimes(n):
    
    if n < 3:
        return 0
    
    result = [True]*n
    result[0] = result[1] = False
    
    for i in range(2, int(math.sqrt(n))+1):
        if result[i] == True:
            print(i, result[i*i:n:i])
            result[i*i:n:i] = [False] * len(result[i*i:n:i])
    return sum(result)
