-- 프로그래머스 No.132202 진료과별 총 예약 횟수 출력하기
select mcdp_cd as "진료과코드", count(*) as "5월예약건수" from appointment 
    where month(apnt_ymd) = "5"
    group by mcdp_cd
    order by count(*), mcdp_cd
;