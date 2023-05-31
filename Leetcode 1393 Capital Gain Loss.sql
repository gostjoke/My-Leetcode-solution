'''
@explain      :
@date         :2023/05/31 16:56:31
'''

# Write your MySQL query statement below
select stock_name,
  sum(case
    When operation = "Buy" Then price*-1 
    else price
  End) as capital_gain_loss
from Stocks
group by stock_name