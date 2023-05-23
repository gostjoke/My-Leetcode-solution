'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

@file         :Leetcode 0034 Find First and Last Position of Element in Sorted Array.py
@explain      :
@date         :2023/05/23 15:03:55
@version      :1.0
'''


# Write your MySQL query statement below

select p.product_name, s.year, s.price from Sales s
left join Product p
on s.product_id = p.product_id
