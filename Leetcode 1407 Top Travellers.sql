'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/25 16:11:12
@version      :1.0
'''


# Write your MySQL query statement below
select u.name, 
case When r.travelled_distance is Null then 0
else r.travelled_distance End as travelled_distance
from Users as u
left join (select user_id, sum(distance) as travelled_distance from Rides group by user_id) as r
on u.id = r.user_id
order by travelled_distance desc, name