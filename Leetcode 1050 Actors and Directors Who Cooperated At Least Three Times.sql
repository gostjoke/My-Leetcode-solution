'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 10:37:38
@version      :1.0
'''


# Write your MySQL query statement below
select actor_id, director_id from 
(select actor_id, director_id, count(`timestamp`) as n from ActorDirector
group by actor_id, director_id) as t
where t.n >= 3