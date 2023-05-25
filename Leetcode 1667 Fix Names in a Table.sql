'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/25 14:53:12
@version      :1.0
'''


# Write your MySQL query statement below
select user_id, concat(upper(substring(name, 1,1)), lower(substring(name, 2))) as name from Users
order by user_id