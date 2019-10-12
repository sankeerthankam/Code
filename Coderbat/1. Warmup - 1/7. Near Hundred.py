# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  i = 10
  if n in range(100-i, 100+i+1) or  n in range(200-i, 200+i+1) :
    return True
  else:
    return False
