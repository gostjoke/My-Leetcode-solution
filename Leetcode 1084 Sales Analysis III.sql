# Write your MySQL query statement below
select distinct ans.product_id, Product.product_name from
(select s1.product_id from
(select s1.product_id, s1.sale_date
from Sales as s1
where s1.sale_date >= "2019-01-01" and s1.sale_date <= "2019-03-31") as s1
left join
(select s2.product_id, s2.sale_date
from Sales as s2
where s2.sale_date < "2019-01-01" or s2.sale_date > "2019-03-31") as s2
on s1.product_id =s2.product_id
where s2.product_id is null) as ans
left join Product
on ans.product_id = Product.product_id
