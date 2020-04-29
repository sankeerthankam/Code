SELECT 
    t1.team_id, t1.team_name, 
    SUM(CASE 
        WHEN t1.team_id = t2.host_team AND t2.host_goals > t2.guest_goals THEN 3
        WHEN t1.team_id = t2.guest_team AND t2.host_goals < t2.guest_goals THEN 3
        WHEN t2.host_goals = t2.guest_goals THEN 1
        ELSE 0
    END) AS num_points
FROM
    Teams t1
LEFT JOIN 
    Matches t2
ON
    t1.team_id = t2.host_team OR
    t1.team_id = t2.guest_team
GROUP BY 1, 2
ORDER BY 3 DESC, 1 ASC
