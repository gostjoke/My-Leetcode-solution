'''
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@date         :2023/05/24 13:52:38
@version      :1.0
'''


# Write your MySQL query statement below
select x,y,z,if(x+y>z and x+z>y and y+z>x, 'Yes','No') as triangle from Triangle