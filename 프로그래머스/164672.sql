-- 프로그래머스 No.164672 조건에 부합하는 중고거래 상태 조회
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
    case
        when status = "SALE"
        then "판매중"
        when status = "RESERVED"
        then "예약중"
        when status = "DONE"
        then "거래완료"
        else "default"
    end as STATUS
    from USED_GOODS_BOARD where CREATED_DATE = "2022-10-05" order by board_id desc