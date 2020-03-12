-- Approach 1
-- Order salary descending and limit 2
-- Order salary ascending from above derived table and Select the second highest salary 

select a.Salary as SecondHighestSalary from (select Salary from Employee order by Salary desc limit 2) a order by salary asc limit 1

-- Approach 2
-- Above approach works only when there are two highest salaries
-- What if there are nulls?
-- Approach 1 does not return null 

select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee) limit 1


-- Run the below query to get third highest, Same query is applicable for nth highest salary just change at rownum<=n-1 .
-- Approach:
  -- Order the salaries
  -- Assign a row num to all the salaries
  -- Extract subset of salaries where row_num is < 3 [This gives top 2 salaries]
  -- Now, extract max(salary) from Employee table where the salary is not in above sub_table.
  
  -- Example:
  -- Actual Salaries: [100, 200, 110, 120, 300]
  -- Ordered Salaries: [300, 200, 120, 110, 100]
  -- {
      1: 300,
      2: 200,
      3: 120,
      4: 110,
      5: 100
  -- }
  -- Subset of top 2 salaries: [300, 200]
  -- max([120, 110, 100]) 
  -- 120
select max(salary) from employee
where salary not in (
  select salary from 
    (select DISTINCT salary from employee order by salary desc)
where rownum<=2);
