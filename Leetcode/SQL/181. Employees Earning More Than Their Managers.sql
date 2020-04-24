# Write your MySQL query statement below

SELECT 
    e1.Name as Employee
FROM 
    Employee e1
LEFT JOIN 
    Employee e2
ON 
    e1.ManagerId = e2.Id
WHERE 
    e1.Salary > e2.Salary
------------------------------------------------------------------------

select 
    e1.Name as Employee -- , e1.Salary, e1.ManagerId, e2.Id, e2.Name as Manager, e2.Salary as ManagerSal
from 
    Employee e1, Employee e2 
where 
    e1.ManagerId = e2.Id
    AND e1.Salary > e2.Salary
