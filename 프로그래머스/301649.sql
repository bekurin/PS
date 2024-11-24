# 프로그래머스 No.301649 대장균의 크기에 따라 분류하기 2
with calcurate_percent_of_size_of_colony as (
    select
        id,
        percent_rank() over (order by size_of_colony desc) as percent
    from ECOLI_DATA
)

select
    id,
    case
        when percent <= 0.25 then 'CRITICAL'
        when percent <= 0.50 then 'HIGH'
        when percent <= 0.75 then 'MEDIUM'
        else 'LOW'
        end as 'COLONY_NAME'
from calcurate_percent_of_size_of_colony
order by id
;
