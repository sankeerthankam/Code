-- Your challenge is to develop a feature that suggests individual movies from Amazon's content database that fit within a given flight's duration. For flight 101, find movies whose runtime is less than or equal to the flight's duration.

-- The output should list suggested movies for the flight, including 'flight_id', 'movie_id', and 'movie_duration'."
-- Tables
-- entertainment_catalog
-- flight_schedule

-- entertainment_catalog
-- duration:bigintmovie_id:biginttitle:text

-- flight_schedule
-- flight_date:dateflight_duration:bigintflight_id:bigint

with cte as 
(
    select * from flight_schedule f
    left join entertainment_catalog e on 
    f.flight_duration >= e.duration
    where duration <= flight_duration 
    -- Important to add where condition here to ensure movie duration is less than the flight duration 
    and flight_id = 101
)
select 
    flight_id, movie_id, duration as movie_duration
from 
    cte
