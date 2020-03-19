# Write your MySQL query statement below

# Approach 1:
# Perform left join on table_1 and table_2

select 
    Person.FirstName, Person.LastName, 
    Address.City, Address.State 
from 
    Person left join 
    Address
on 
    Person.PersonId = Address.PersonId
