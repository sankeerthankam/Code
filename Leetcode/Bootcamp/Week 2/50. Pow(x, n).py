# Approach 1:
# Use **
def pow(x, n):
    return x**n
    
# Approach 2:
# for range in n:
  # Multiple result with x
def poww(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    else:
        if n < 0:
            neg = True
        else:
            neg = False

        res = 1

        for i in range(abs(n)):
            res = res * x

        return 1/res if neg else res
