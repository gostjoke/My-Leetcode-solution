'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/25 16:11:12
@version      :1.0
'''
 

# Write your MySQL query statement below
select 
    user_id, 
    Max(time_stamp) as last_stamp from Logins
where year(time_stamp) = 2020
group by user_id;