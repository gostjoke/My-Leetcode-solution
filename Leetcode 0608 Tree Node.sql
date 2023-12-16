# Write your MySQL query statement below
select id,
    case
        when p_id is Null Then 'Root'
        when id in (select p_id from Tree) then 'Inner'
        else 'Leaf'
        End as type
from Tree
