'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/23 14:36:38
@version      :1.0
'''

# Write your MySQL query statement below
select id, movie, description, rating from Cinema
where id % 2 = 1 and description <> 'boring'
order by rating desc