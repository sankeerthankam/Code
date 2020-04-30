-- Approach 1
  -- Employee (Employee Name)
  --  LEFT JOIN
  -- Employee (Department and Max Salary)
  --  LEFT JOIN
  -- Department (Department Name)
-- Cons: Less Than 5% time complexity
SELECT
    t3.Name as Department, t1.Name as Employee, t1.Salary
FROM 
    Employee t1,

    (SELECT 
        DepartmentId, MAX(Salary) as Salary
    FROM
        Employee
    GROUP BY 
        1) t2,
    Department t3
WHERE 
    t1.DepartmentId = t2.DepartmentId 
    AND t1.Salary = t2.Salary
    AND t1.DepartmentId = t3.Id
    
    
    
-- Approach 2
-- Employee 
  -- LEFT JOIN 
-- Department
--   (dempartment_id, salary) = (department_id, max(salary)
SELECT 
    t2.Name AS Department, t1.Name AS Employee, t1.Salary 
from 
	Employee t1,
	Department t2 
WHERE 
    t1.DepartmentId = t2.id 
    AND (DepartmentId, Salary) in 
    (SELECT DepartmentId, max(Salary) FROM Employee GROUP BY 1)
