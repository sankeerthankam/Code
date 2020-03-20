# Write your MySQL query statement below


select 
    e1.Name as Employee -- , e1.Salary, e1.ManagerId, e2.Id, e2.Name as Manager, e2.Salary as ManagerSal
from 
    Employee e1, Employee e2 
where 
    e1.ManagerId = e2.Id
    AND e1.Salary > e2.Salary
