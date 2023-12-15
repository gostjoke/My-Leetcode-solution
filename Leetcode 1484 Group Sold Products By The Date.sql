select 
    sell_date, 
    count(product) as num_sold,
    string_agg(product, ',' order by product) as products
from (
    select distinct sell_date, product
    from Activities
    )
group by sell_date
order by sell_date
