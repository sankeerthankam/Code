# Approach 1:
# Sub Query 1: Extract all posts (where parent id is null)
# Sub Query 2: Extract number of comments for all posts (parent_id, count(distinct(*)) where parent id is not null, group by 1)
# Join two sub queries

SELECT 
    s1.sub_id AS post_id, 
    CASE   
        WHEN s2.cnt IS NULL THEN 0
        ELSE s2.cnt 
    END AS number_of_comments
FROM 
    (SELECT * FROM Submissions WHERE parent_id IS NULL) s1
LEFT JOIN
    (SELECT parent_id, COUNT(DISTINCT(sub_id)) AS cnt FROM Submissions WHERE parent_id IS NOT NULL GROUP BY 1) s2
ON 
    s1.sub_id = s2.parent_id
GROUP BY 
    1
ORDER BY 
    1
