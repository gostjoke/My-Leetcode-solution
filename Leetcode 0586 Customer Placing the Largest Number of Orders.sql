'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/23 14:20:38
@version      :1.0
'''

# Write your MySQL query statement below
select t1.customer_number from
(select count(order_number) as count_dinner,customer_number from Orders
group by customer_number 
order by count_dinner desc
limit 1) t1

'''
faster second way
'''
select customer_number from Orders 
group by customer_number order by count(customer_number) desc limit 1
