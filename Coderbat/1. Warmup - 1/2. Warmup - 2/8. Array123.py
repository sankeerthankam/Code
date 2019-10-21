# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  # using a generator to convert a numeric array to string
  gen = ''.join((str(i) for i in nums))
  return '123' in gen
