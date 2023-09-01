-- 프로그래머스 No.164668 조건에 맞는 사용자와 총 거래금액 조회하기
select USER_ID, NICKNAME, sum(price) as TOTAL_SALES from used_goods_board as ugb
    inner join used_goods_user as ugu on ugu.user_id = ugb.writer_id
    where ugb.STATUS = "DONE"
    group by writer_id
    having TOTAL_SALES >= 700000
    order by TOTAL_SALES
;