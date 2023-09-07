-- 프로그래머스 No.144855 카테고리 별 도서 판매량 집계하기
select CATEGORY, sum(sales) as TOTAL_SALES from book
    inner join book_sales on book_sales.book_id = book.book_id
    where year(sales_date) = 2022 and month(sales_date) = 1
    group by category
    order by category