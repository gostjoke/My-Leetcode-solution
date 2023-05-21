
'''
@explain      :
@date         :2023/05/21 13:22:20
@author       : 
@version      :1.0
'''

"MySQL"

"# Write your MySQL query statement below"
select Distinct(p1.email) from Person p1, Person p2
where p1.id <> p2.id and p1.email = p2.email