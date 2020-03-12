-- Approach 1
-- Order salary descending and limit 2
-- Order salary ascending from above derived table and Select the second highest salary 

select a.Salary as SecondHighestSalary from (select Salary from Employee order by Salary desc limit 2) a order by salary asc limit 1

-- Approach 2
-- Above approach works only when there are two highest salaries
-- What if there are nulls?
-- Approach 1 does not return null 

select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee) limit 1
-- select salary as SecondHighestSalary from Employee order by salary desc limit 1, 1
