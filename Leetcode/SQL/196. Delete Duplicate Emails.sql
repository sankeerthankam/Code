# Approach 1
# SubQuery 1: Extract the records you want to include
# Subquery 2: Delete records whose id not in (subquery 1)

DELETE FROM Person
WHERE Id 
NOT IN (SELECT Id FROM 
            (SELECT MIN(Id) AS Id FROM Person GROUP BY Email) p
        );
        
# Approach 2
# Join p1 and p2 (self join) 
# Delet p1 where p1.Id > p2.Id and p1.email = p2.email

DELETE 
    p1
FROM 
    Person p1, Person p2
WHERE 
    p1.Email = p2.Email AND
    p1.Id > p2.Id
