-- 프로그래머스 No.164670 조건에 맞는 사용자 정보 조회하기
select ugu.user_id as USER_ID, ugu.nickname as NICKNAME, concat(ugu.city, ' ', ugu.street_address1, ' ', ugu.street_address2) as '전체주소', concat(substr(ugu.tlno, 1,3), "-", substr(ugu.tlno, 4,4), "-", substr(ugu.tlno, 8,4)) as '전화번호' from used_goods_board as ugb
    inner join used_goods_user as ugu on ugu.user_id = ugb.writer_id
    group by ugu.user_id
    having count(*) >= 3  order by ugu.user_id desc
;