-- 코드를 입력하세요
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
FROM used_goods_board b JOIN used_goods_reply r ON b.board_id = r.board_id
WHERE b.CREATED_DATE >= '2022-10-01'
  AND b.CREATED_DATE <  '2022-11-01'
--  AND r.CREATED_DATE >= '2022-10-01'
-- AND r.CREATED_DATE <  '2022-11-01'
ORDER BY r.created_date , b.title ;