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
https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions
