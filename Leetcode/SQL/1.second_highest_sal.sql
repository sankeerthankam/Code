# Write your MySQL query statement below

select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee) limit 1
-- select salary as SecondHighestSalary from Employee order by salary desc limit 1, 1
