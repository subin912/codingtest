-- 코드를 입력하세요
SELECT f.flavor #(f.total_order + j.total_order)
FROM FIRST_HALF f JOIN (
    SELECT flavor,sum(total_order) as total_order
    FROM JULY
    GROUP BY flavor) j ON f.flavor = j.flavor
ORDER BY f.total_order + j.total_order desc
LIMIT 3;
