'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

@date         :2023/05/23 15:10:55
@version      :1.0
'''

# Write your MySQL query statement below
select w2.id from Weather w1
inner join Weather w2
where w2.temperature > w1.temperature and Datediff(w2.recordDate, w1.recordDate) = 1
