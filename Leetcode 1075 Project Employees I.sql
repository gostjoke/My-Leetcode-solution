'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/23 15:17:38
@version      :1.0
'''


# Write your MySQL query statement below
select p.project_id, round(avg(experience_years),2) as average_years from Project p
left join employee e
on e.employee_id = p.employee_id 
group by p.project_id