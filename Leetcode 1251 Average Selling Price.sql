-- 04/19/2024
-- Write your MySQL query statement below3
-- select u.product_id, 
-- round(sum(price * units)/sum(units), 2) as average_price
select t1.product_id, sum(t1.average_price) as average_price
from
(select p.product_id, 
case 
    when round(sum(price * units)/sum(units), 2) is null then 0
    else round(sum(price * units)/sum(units), 2) 
end as average_price
from prices as p
left join unitssold as u
    on p.product_id = u.product_id 
    and u.purchase_date between p.start_date and p.end_date
group by u.product_id) as t1
group by t1.product_id

