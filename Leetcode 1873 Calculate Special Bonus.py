'''
07/07/2023
'''

# Write your MySQL query statement below
select t.employee_id, t.bonus from 
(select employee_id, salary as bonus from Employees
where employee_id % 2 = 1 and name not like 'M%'
union
select employee_id, 0 as bonus from Employees
where employee_id % 2 = 0 or name like 'M%') as t
order by t.employee_id
