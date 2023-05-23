'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/23 15:32:38
@version      :1.0
'''

# Write your MySQL query statement below
# select departmentId, MAX(Salary) as Salary from employee group by departmentid

select Department.name as Department, Employee.name as Employee, Employee.Salary from department
join employee on employee.departmentId = department.id
where (departmentId, Salary) in (select departmentId, MAX(Salary) as Salary from employee group by departmentid);