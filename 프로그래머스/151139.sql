-- 프로그래머스 No.151139 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기
select month(start_date) as MONTH, CAR_ID, count(*) as RECORDS from car_rental_company_rental_history
    where car_id in (select car_id from car_rental_company_rental_history
                        where start_date between "2022-08-01" and "2022-10-31"
                        group by car_id
                        having count(*) >= 5
                    )
    and start_date between "2022-08-01" and "2022-10-31"
    group by MONTH, car_id
    order by MONTH, car_id desc
;