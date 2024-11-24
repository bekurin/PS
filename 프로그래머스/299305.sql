# 프로그래머스 No.299305 대장균의 자식의 수 구하기
select
    ed1.id,
    count(ed2.parent_id) as CHILD_COUNT
from ECOLI_DATA as ed1
         left join ECOLI_DATA as ed2 on ed2.parent_id = ed1.id
group by ed1.id
;
