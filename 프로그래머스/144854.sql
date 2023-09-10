-- 프로그래머스 No.144854 조건에 맞는 도서와 저자 리스트 출력하기
select BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE from book
    inner join author on author.author_id = book.author_id
    where category = "경제"
    order by published_date
;