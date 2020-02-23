# Approach:
# https://www.youtube.com/watch?v=7kYlJRSoQqQ
# NOTE: 1 is always an ugly number
# First element in the sequence will always be 1
# [1]
# Next element will be a factor of 2, 3 or 5 
# Which means
# Next element in the sequence will be one of the (2*i, 3*i, 5*i)
# Pay attention to i in the above sentence -> We cannot use the same pointer to keep track of factors of 2,3 and 5
# Hence we need three points to keep track of factors of 2, 3 and 5 individually.
# So, it would be pointers (i, j, k)

# Now, the next element in the sequence will be one of the (2*i, 3*j, 5*k)
# More specifically -> Next ele = min(2*1, 3*1, 5*1) i.e. min(2, 3, 5) = 2
# Keep incrementing the index (i, j, k) for every iteration in the loop

def nthUglyNumber(n):
  res = [1]
  i = j = k = 0
  count = 0

  while count < n:
      val = min(res[i]*2,min(res[j]*3,res[k]*5))
      if val == res[i]*2:
          i+=1
      if val == res[j]*3:
          j+=1
      if val == res[k]*5:
          k+=1
      count+=1
      if count == n:
          return res[-1]
      res.append(val)
