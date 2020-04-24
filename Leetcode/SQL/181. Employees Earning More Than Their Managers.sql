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

-- Improvements:
-- The above approach scans the atble twice - Instead you can extract the list of managers beforehand using distinct and id != numm (this eliminates duplicate and null records)
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/discuss/406403/Faster-than-96-Using-subquery
