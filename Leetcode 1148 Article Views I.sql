#!/usr/bin/env 
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/31 14:05:10
@version      :1.0
'''
 
# Write your MySQL query statement below
select distinct(author_id) as id from Views
where  author_id = viewer_id
order by id