-- Approach 1

SELECT 
  DISTINCT l1.Num 
FROM 
  Logs l1, Logs l2, Logs l3 
WHERE 
  l1.Id = l2.Id-1 AND 
  l2.Id = l3.Id-1 AND 
  l1.Num = l2.Num AND 
  l2.Num=l3.Num

-- Approach 2

SELECT 
  DISTINCT Num as ConsecutiveNums
FROM 
  Logs
WHERE 
  (Id + 1, Num) in (select * from Logs) AND 
  (Id + 2, Num) in (select * from Logs)
