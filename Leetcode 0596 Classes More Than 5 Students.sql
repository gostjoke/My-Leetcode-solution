'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/23 14:30:38
@version      :1.0
'''

# Write your MySQL query statement below
select t1.class from
(select count(student) as no, class from Courses 
group by class) as t1
where t1.no >= 5