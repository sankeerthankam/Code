# Write your MySQL query statement below
SELECT
    t1.Name as Customers
FROM
    Customers t1
WHERE
    t1.Id NOT IN
    (SELECT
        DISTINCT CustomerID
    FROM
        Orders)
