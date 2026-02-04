-- 코드를 입력하세요
SELECT i.name, i.datetime
FROM ANIMAL_INS i LEFT JOIN ANIMAL_OUTS o ON i.animal_id = o.animal_id
WHERE o.animal_id IS NULL
ORDER BY i.datetime
LIMIT 3;

#3개만 조회하는 SQL 코드 즉 상위 3건만 보고 싶을 때