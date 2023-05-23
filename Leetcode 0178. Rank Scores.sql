'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/23 15:55:38
@version      :1.0
'''

# Write your MySQL query statement below
SELECT s.Score as score,
Dense_RANK() OVER (ORDER BY s.Score DESC) as `rank`
FROM Scores s

## second way
Select s1.score , s2.`rank` from Scores s1
left join 
(select s2.score, rank() over(order by score desc) as `rank` from
(SELECT DISTINCT score FROM Scores) s2) as s2
on s1.score = s2.score
order by `rank`
