'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/25 15:26:12
@version      :1.0
'''


# Write your MySQL query statement below
select
    case
        WHEN seat.id % 2 <> 0 and seat.id = (select count(*) from seat) then seat.id  "deal last one"
        when seat.id % 2 = 0 THEN seat.id - 1  "deal not odd"
        Else
            seat.id + 1 "deal odd"
    END as id,
    student
from seat
order by id
