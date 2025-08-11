-- 20250811
# Write your MySQL query statement below
select 
    s.student_id, 
    s.student_name, 
    su.subject_name, 
    count(e.subject_name) as attended_exams
from Students as s
join Subjects as su
left join Examinations as e
on s.student_id = e.student_id and su.subject_name = e.subject_name
group by s.student_id, su.subject_name
order by s.student_id, su.subject_name
