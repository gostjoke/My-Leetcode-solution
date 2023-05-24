'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 14:28:12
@version      :1.0
'''


# Write your MySQL query statement below
select customer_id
from Customer 
group by customer_id
having count(distinct product_key) = (select count(distinct product_key) from Product)