'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 14:53:12
@version      :1.0
'''


# Write your MySQL query statement below
select D.name as Department, t1.name as Employee, t1.Salary from
(select *, DENSE_RANK() over(partition by departmentId order by salary desc) as `rank`
from Employee) as t1
left join Department as D
on t1.departmentId = D.id
where t1.`rank` < 4