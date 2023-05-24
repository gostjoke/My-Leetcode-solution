'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 12:07:38
@version      :1.0
'''


# Write your MySQL query statement below
select e2.unique_id, e1.name from Employees as e1
left join EmployeeUNI as e2
on e1.id = e2.id