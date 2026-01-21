# 2026/01/20
# Write your MySQL query statement below
select 
    e2.employee_id, e2.name, count(e.reports_to) as reports_count, round(avg(e.age), 0) as average_age
from 
    Employees as e
left join Employees as e2 on e.reports_to = e2.employee_id
where e.reports_to is not null
group by e.reports_to
order by e2.employee_id
