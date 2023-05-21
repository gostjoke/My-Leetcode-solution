
'''
@explain      :
@date         :2023/05/21 12:39:20
@author       : 
@version      :1.0
'''

"MySQL"

select A.player_id, min(A.event_date) as first_login from Activity as A
group by A.player_id