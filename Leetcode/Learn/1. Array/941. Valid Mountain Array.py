# Approach 1
# Read the ccomments

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

# Approach 2
# Use two pointers flag1 and flag2
# Update flag1 = True at the end of the increment peak
# Update flag2 = True at the end of the decrement peak
# return (flag1 and flag2) which will return True if both are True

def validMountainArray(A):
  flag1 = False
  flag2 = False
  for i in range(len(A)-1):
      if A[i]==A[i+1]:
          return False
      elif A[i]<A[i+1]:
          if flag2==True:
              return False
          flag1=True
      elif A[i]>A[i+1]:
          flag2=True
  return flag1 and flag2
