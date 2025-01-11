# 2025/01/11
# Write your MySQL query statement below
# so stupid...
select Signups.user_id, COALESCE(t3.confirmation_rate, 0) as confirmation_rate 
from Signups left join
(select t1.user_id, Round(t2.confirm/t1.a_action, 2) as confirmation_rate from
    (select user_id, count(action) as a_action from Confirmations
        group by user_id) as t1
        left join
            (select user_id, count(action) as confirm from Confirmations
                where action = 'confirmed'
                group by user_id) as t2
                on t1.user_id = t2.user_id) as t3
on t3.user_id = Signups.user_id
order by confirmation_rate


## Chatgpt improved this
SELECT 
    S.user_id, 
    COALESCE(ROUND(CASE 
                     WHEN C.a_action = 0 THEN 0 
                     ELSE C.confirm / C.a_action 
                   END, 2), 0) AS confirmation_rate
FROM 
    Signups S
LEFT JOIN (
    SELECT 
        user_id, 
        COUNT(action) AS a_action,
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirm
    FROM Confirmations
    GROUP BY user_id
) AS C
ON S.user_id = C.user_id
ORDER BY confirmation_rate;
