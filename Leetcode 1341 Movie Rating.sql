# 12/14/2023
# Write your MySQL query statement below
(
    select u.name as results 
    from MovieRating as mr
    left join Users as u
    on mr.user_id = u.user_id  
    group by mr.user_id
    order by count(mr.user_id) desc, u.name
    limit 1
)
union all
(
  select m.title as results 
  from MovieRating as mr
  left join Movies as m
  on mr.movie_id = m.movie_id
  group by mr.rating
  order by avg(mr.rating) desc
  limit 1
)
