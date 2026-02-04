-- 코드를 입력하세요
SELECT o.animal_id, o.name
FROM ANIMAL_INS i RIGHT JOIN ANIMAL_OUTS o ON i.animal_id = o.animal_id
WHERE i.animal_id IS NULL
ORDER BY o.animal_id;