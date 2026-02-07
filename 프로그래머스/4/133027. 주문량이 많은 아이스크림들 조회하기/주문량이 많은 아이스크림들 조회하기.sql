-- 코드를 입력하세요
SELECT f.flavor
FROM FIRST_HALF f JOIN JULY j ON f.flavor = j.flavor
GROUP BY flavor
ORDER BY SUM(f.total_order) DESC
limit 3;