# Approach 1

def merge(intervals):
  # Check edge case
  if not intervals:   
      return []

  # Sort the list to make it ascending with respect to the sub-list's first element and then in second element
  intervals = sorted(intervals) 
  # Initialize the result list with the first sub-list
  res = [intervals[0]]    

  # Traverse the entire sorted list from the 2nd sub-list
  for i in range(1, len(intervals)): 
      # There is intersection, then update the last sub-list of result
      if intervals[i][0] <= res[-1][1]:  
          res[-1][1] = max(res[-1][1], intervals[i][1])
      
      # There is no intersection, then append the current sub-list to result
      else:   
          res.append(intervals[i])

  return res
  
  
def merge(intervals):
  if len(intervals) == 0:
      return []
    
  intervals.sort()

  i, res = 0, []
  while i < len(intervals)-1:
      if intervals[i][1] < intervals[i+1][0]:
          res.append(intervals[i])

      elif intervals[i][1] >= intervals[i+1][0] and intervals[i][1] < intervals[i+1][1]:
          intervals[i+1][0] = intervals[i][0]

      else:
          intervals[i+1][0] = intervals[i][0]
          intervals[i+1][1] = intervals[i][1]

      i += 1

  res.append(intervals[i])
  return res
