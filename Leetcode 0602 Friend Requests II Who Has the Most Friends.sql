'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 11:47:38
@version      :1.0
'''


# Write your MySQL query statement below
select t1.id, count(t1.accept_date) as num from
(select requester_id as id, accept_date  from RequestAccepted
union all
select accepter_id as id , accept_date from RequestAccepted) as t1
group by t1.id
order by num desc
limit 1