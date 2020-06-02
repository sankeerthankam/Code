# Approach 1
# Sort and traverse through intervals
# If the intervals start_time is greater than end_time of last element in results
  # do nothing i.e. append the interval as is
# Else
  # update the end_time of the last ele to max(end_time of last ele, end_time of interval)

def insert(intervals, newInterval):
  intervals.append(newInterval)
  intervals.sort(key=lambda x: x[0])

  result = []
  for interval in intervals:
      if not result or result[-1][1] < interval[0]:
          result.append(interval)
      else:
          result[-1][1] = max(result[-1][1],interval[1])

  return result
        
# Approach 2
# Divide intervals into two buckets left and right
# Left bucket -> All intervals whose end time is less than start_time of new interval
# Right bucket -> All intervals whose start time is greater than end_time of new interval

# If an interval does not fall in one of these buckets, you have update your start and end time.

# https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions
def insert(intervals, newInterval):
  start = newInterval[0]
  end = newInterval[1]
  left = []
  right = []
  new_interval = []
  for i in intervals:
      if i[1] < start:
          # left.append(i)
          left += [i]
      elif i[0] > end:
          # right.append(i)
          right += [i]
      else:
          start = min(i[0], start)
          end = max(i[1], end)

  new_interval.append(start)
  new_interval.append(end)

  return left + [new_interval] + right 
