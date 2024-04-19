-- 04/19/2024
-- Write your MySQL query statement below
select person_name
from Queue as q1
where
(
    select sum(weight) from Queue as q2
    where q2.turn <= q1.turn
    order by turn
) <= 1000
order by q1.turn desc limit 1;

