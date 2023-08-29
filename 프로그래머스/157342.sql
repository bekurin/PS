-- 프로그래머스 No.157342 자동차 평균 대여 기간 구하기
select CAR_ID, round(sum(datediff(end_date, start_date) + 1)/count(*), 1) as 'AVERAGE_DURATION'
    from car_rental_company_rental_history
    group by car_id
    having AVERAGE_DURATION >= 7
    order by AVERAGE_DURATION desc, car_id desc