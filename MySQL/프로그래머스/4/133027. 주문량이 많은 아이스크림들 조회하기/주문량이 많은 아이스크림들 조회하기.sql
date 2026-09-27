-- 코드를 입력하세요
SELECT f.FLAVOR
FROM first_half f join july j on f.FLAVOR = j.FLAVOR
GROUP BY FLAVOR
ORDER BY sum(f.total_order+j.total_order) desc
LIMIT 3;