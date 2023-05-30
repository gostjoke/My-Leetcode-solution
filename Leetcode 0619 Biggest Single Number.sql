'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/30 16:11:12
@version      :1.0
'''
 

# Write your MySQL query statement below
select Max(t1.num) as num from 
(select num from MyNumbers
group by num
having count(num) = 1) as t1