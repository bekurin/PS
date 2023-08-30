-- 프로그래머스 No.164671 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
select concat('/home/grep/src/', board_id, '/', file_id, file_name, file_ext) as 'FILE_PATH' from used_goods_file as ugf
    where board_id = (select board_id from used_goods_board as ugb order by views desc limit 1) 
    order by file_id desc
;