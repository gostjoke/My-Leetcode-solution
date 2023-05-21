#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@explain      :
@date         :2023/05/21 11:31:20
@author       : 
@version      :1.0
'''


# Write your MySQL query statement below
select Person.firstName, Person.lastName, Address.city, Address.state from Person
left join Address
on Person.personId = Address.personId