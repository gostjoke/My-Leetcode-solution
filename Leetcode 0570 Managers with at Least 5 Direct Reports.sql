'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 10:47:38
@version      :1.0
'''


# Write your MySQL query statement below
select name from Employee as e
left join
(select id, name as name2, count(department) as departcount, managerId from Employee
group by managerId) as t2
on e.id = t2.managerId
where departcount >= 5