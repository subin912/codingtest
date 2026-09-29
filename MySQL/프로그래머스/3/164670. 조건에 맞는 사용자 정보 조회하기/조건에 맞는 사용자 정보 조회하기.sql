-- 코드를 입력하세요
SELECT u.user_id, u.nickname, 
    concat(u.city,' ',u.street_address1,' ',u.street_Address2) AS '전체주소', 
    concat(left(u.tlno,3),'-',substring(u.tlno,4,4),'-',right(u.tlno,4)) AS '전화번호'
FROM USED_GOODS_BOARD b RIGHT JOIN USED_GOODS_USER u ON b.writer_id = u.user_id
GROUP BY u.user_id
HAVING count(u.user_id) >= 3
ORDER BY u.user_id DESC;