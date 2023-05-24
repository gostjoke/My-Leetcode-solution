'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 14:33:12
@version      :1.0
'''


# Write your MySQL query statement below
select teacher_id, count(distinct subject_id) as cnt from Teacher
group by teacher_id