-- 코드를 작성해주세요
# 3세대의 대장균의 ID 출력하는 SQL문
SELECT p3.id
FROM ECOLI_DATA p1 
LEFT JOIN ECOLI_DATA p2 ON p1.id = p2.parent_id
LEFT JOIN ECOLI_DATA p3 ON p2.id = p3.parent_id
WHERE p1.parent_id is null
AND p3.id IS NOT NULL;
# 2세대인 애들을 부모로 가지는 애들
# 즉 WHERE 2세대를 찾고 그다음에 3세대 찾자
# 다른 행을 참조하기에 - SELF JOIN