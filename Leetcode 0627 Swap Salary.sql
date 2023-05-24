'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 10:36:38
@version      :1.0
'''

# Write your MySQL query statement below
# Write your MySQL query statement below
UPDATE Salary
SET sex = 
CASE sex
    when 'm' then 'f'
    when 'f' then 'm'
End;