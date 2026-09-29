-- 코드를 입력하세요
SELECT substring(product_code,1,2) AS CATEGORY, count(*) AS PRODUCTS
FROM PRODUCT
GROUP BY substring(product_code,1,2)
ORDER BY CATEGORY;