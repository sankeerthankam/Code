# Approach 1:
# Covers corner cases where x + y == 0 and x + y < z
# Find the gcd of x and y
  # Note: GCD of co-primes is always 1
# Then check if z is multiple of gcd(x, y)

def canMeasureWater(x, y, z):
    if x + y < z:
        return False

    else:
        if x + y == 0:
            return True
        else:
            import math
            g = math.gcd(x, y)

            # Check if z is a multiple of g (gcd of x and y)
            if z % g == 0:
                return True
            else:
                return False

            # return not(z % g)

# Approach 2:
# Same as Approach 1 but we do not cover the corner cases and we have a separate function for is_multiple.

def canMeasureWater(x, y, z):
  def is_multiple(x, y):
    return x and (y % x) == 0

   import math
   g = math.gcd(x, y)

   # Check if z is a multiple of g (gcd of x and y)
   return is_multiple(g, z) 

  # To get the coefficients of x, y when they will be equal to z :
  # https://leetcode.com/problems/water-and-jug-problem/discuss/83715/Math-solution-Java-solution
