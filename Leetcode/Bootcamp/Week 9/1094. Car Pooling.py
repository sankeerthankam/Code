# Approach 1:
# If at any point, the number of current passengers of our car is greater than capacity we can return False.
# trips = [[2,1,5],[3,5,7]]    # [Number of Passengers, Start Time, End Time] 

# time : net change in passengers
# 1  :  +2      # At event time 1, we pick up 2 passengers
# 5  :  +1      # At event time 5, we drop off 2 passengers and pick up 3 (net +1)
# 7  :  -3      # At event time 7, we drop off 3 passengers 

# Then we sort these events by start time because the order matters. We need to process events at time 1 before we process events at time 7.
# Now we can simply iterate over the events and add the net change to our current number of passengers. If the current number of passengers ever exceeds capacity, return False.

def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
  from collections import defaultdict
  dd = defaultdict(int)
  for trip in trips:
      num, start, end = trip
      dd[start] += num
      dd[end] -= num

  # Passanger movement for each time timestamp
  passangers = [count for time, count in sorted(dd.items())]

  current_count = 0
  for p in passangers:
      current_count = current_count + p
      if current_count > capacity:
          return False
  return True


# Doesn't work
def carPooling(trips, capacity):
    available_capacity = 0
    for i in range(len(trips)-1):
        start_time_1 = trips[i][1]
        end_time_1 = trips[i][2]
        start_time_2 = trips[i+1][1]
        end_time_2 = trips[i+1][2]
        
        if end_time_1 > start_time_2:
            if trips[i][0] + trips[i+1][1] > capacity:
                return False
            else:
                continue
#                 available_capacity = capacity - i[0]
    return True


# Approach 2:
# Naive approach
# Doesn't address corner cases.
def carPooling(trips, capacity):
    from collections import defaultdict
    dd = defaultdict(int)
    for trip in trips:
        num, start, end = trip
        dd[start] += num
        dd[end] -= num

    # Passanger movement for each time timestamp
    passangers = [count for time, count in sorted(dd.items())]


    current_count = 0
    for p in passangers:
        current_count = current_count + p
        if current_count > capacity:
            return False
    return True

