def validMountainArray(A):
  # Edge Case (Also this is one of the assumption)
  if len(A) < 3: 
      return False
  if A[0] > A[1]:
      return False

  pointer = 0

  # First loop exits after finding the peak value (i.e. condition is "break the loop when you see A[i] > A[i+1]
  for i in range(len(A)-1):
      if A[i] < A[i+1]:
          continue
      else:
          pointer = i
          break

  # Loop from peak to rest of the array
  for i in range(pointer, len(A)-1):
      if A[i] > A[i + 1]:
          continue
      else:
          return False
  return True
