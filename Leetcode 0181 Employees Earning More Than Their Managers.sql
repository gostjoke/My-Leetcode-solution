'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

@explain      :
@date         :2023/05/23 14:57:55
@version      :1.0
'''


# Write your MySQL query statement below
select e2.name as Employee from employee e1
inner join employee e2
on e1.id = e2.managerId
where e1.salary < e2.salary
