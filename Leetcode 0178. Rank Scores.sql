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