-- 코드를 입력하세요
SELECT i.ingredient_type, sum(f.total_order) AS TOTAL_ORDER
FROM FIRST_HALF f JOIN ICECREAM_INFO i ON i.flavor = f.flavor #flavor가 pk, 기본키는 f니까
GROUP BY i.ingredient_type # 맛별로 묶는거 아니고 성분별로 묶음
ORDER BY TOTAL_ORDER ASC;