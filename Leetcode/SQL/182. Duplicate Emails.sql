# Approach 1

SELECT 
    Email
FROM 
    (SELECT Email, Count(Id) as cnt FROM Person GROUP BY 1) a
WHERE
    a.Id > 1
    
    
# Approach 2

SELECT 
    Email
FROM 
    Person
GROUP BY 
    1
HAVING
    count(Id) > 1
