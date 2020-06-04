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
 

# Approach 2 -> Without pointers
  # seperate start_times and end_times and add a flag (0 or 1) to differentiate
  # Combine and sort start_times, end_times
  # Traverse trough all_times:
    # If you see a start_time -> increment the max_so_far
    # If you see an end_time -> decrement the max_so_far
      # Update max_rooms with max(max_so_far, max_rooms)
def minMeetingRooms(intervals):
  start_times = []
  end_times = []
  for i in intervals:
      start_times.append((i[0], 1))
      end_times.append((i[1], 0))

  all_times =  start_times + end_times
  all_times.sort()

  max_so_far = 0
  max_rooms = 0

  for time, event_type in all_times:
      if event_type == 0:
          max_so_far -= 1
      else:
          max_so_far += 1
          max_rooms = max(max_rooms, max_so_far)

        return max_rooms

  
  
# Approach 3 -> With pointers
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

  start_pointer = end_pointer = 0
  max_rooms = available_rooms = 0
  while start_pointer < len(starts):
      if starts[start_pointer] < ends[end_pointer]:
          if available_rooms == 0:
              max_rooms += 1
          else:
              available_rooms -= 1

          start_pointer += 1
      else:
          available_rooms += 1
          end_pointer += 1
  return max_rooms
