#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/05/21 12:39:20
@author       : 
@version      :1.0
'''


' Write your MySQL query statement below '
select max(Salary) as SecondHighestSalary from Employee
where Salary < (Select max(Salary) from Employee)