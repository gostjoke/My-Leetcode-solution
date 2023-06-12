#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :Mysql
@date         :2023/06/12 16:09:19
@version      :1.0
'''


# Write your MySQL query statement below
select t1.employee_id from
((select s.employee_id, e.name, s.salary from Employees as e
Right join Salaries as s
on s.employee_id = e.employee_id)
union
(select e.employee_id, e.name, s.salary from Employees as e
left join Salaries as s
on s.employee_id = e.employee_id)) as t1
where t1.name is null or t1.salary is null
order by t1.employee_id