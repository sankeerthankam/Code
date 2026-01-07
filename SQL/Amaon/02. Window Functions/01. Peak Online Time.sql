-- For each device type, find the time period with the highest number of active users.

-- The output should contain 'user_count', 'time_period', and 'device_type', where 'time_period' is a concatenation of 'start_timestamp' and 'end_timestamp', like ; "start_timestamp to end_timestamp".

-- user_activity
-- device_type:textend_timestamp:timestamp without time zonestart_timestamp:timestamp without time zonetime_difference:double precisionuser_count:bigint


with cte as 
(select 
    device_type, 
    (start_timestamp || ' to ' || end_timestamp) as time_period,
    user_count,
    rank() over(PARTITION BY device_type order by user_count desc) as rnk
    -- Window function syntax
from user_activity
) 
select user_count, time_period, device_type from cte where rnk = 1
