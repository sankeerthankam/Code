# Approach 1
# Compare start and end times 
# But this approach doesn't work for overlapping start and end times
def minMeetingRooms(intervals):
  intervals.sort()
  count = 1
  for i in range(len(intervals)-1):
      if intervals[i][1] > intervals[i+1][0]:
          count = count + 1
  return count
 
# Approach 2
 # Very similar with what we do in real life. Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).

def minMeetingRooms(intervals):
  starts = []
  ends = []
  for i in intervals:
      starts.append(i[0])
      ends.append(i[1])

  starts.sort()
  ends.sort()

  s = e = 0
  numRooms = available = 0
  while s < len(starts):
      if starts[s] < ends[e]:
          if available == 0:
              numRooms += 1
          else:
              available -= 1

          s += 1
      else:
          available += 1
          e += 1

  return numRooms
