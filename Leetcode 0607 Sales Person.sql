'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/25 15:40:12
@version      :1.0
'''


# Write your MySQL query statement below
select name from SalesPerson
where name not in (
select t2.name from 
(select t1.sales_id, t1.name, t1.order_id, t1.com_id, c.name as company_name 
from
  (select s.sales_id, s.name, o.order_id, o.com_id from SalesPerson s
    left join Orders o
    on o.sales_id = s.sales_id) as t1
    left join company c
    on c.com_id = t1.com_id
    where c.name = "RED") as t2)