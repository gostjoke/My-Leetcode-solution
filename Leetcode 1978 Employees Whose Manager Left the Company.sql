'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/25 15:59:12
@version      :1.0
'''


# Write your MySQL query statement below
select employee_id from Employees
where manager_id Not in (select employee_id FROM employees)
and salary < 30000
order by employee_id