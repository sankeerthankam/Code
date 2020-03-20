-- Approach 1
-- Naìve Approach

SELECT TOP 1 Salary
FROM (
      SELECT DISTINCT TOP N Salary
      FROM Employee
      ORDER BY Salary DESC
      ) AS Emp
ORDER BY Salary


-- Approach 2
-- My SQL
SELECT Salary FROM Employee ORDER BY Salary DESC LIMIT n-1,1

-- Approach 3
-- Using Rank
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N-1;
  RETURN (
      select DISTINCT salary from Employee order by salary desc limit M, 1
  );
END
