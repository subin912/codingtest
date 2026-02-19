-- 코드를 입력하세요
SELECT p.product_id, p.product_name, SUM(o.amount * p.price) AS total_sales
FROM FOOD_PRODUCT p JOIN FOOD_ORDER o ON p.product_id = o.product_id
WHERE o.produce_date BETWEEN '2022-05-01' AND '2022-05-31' 
## 2022년 5월에 생산된 식품만 필터링
GROUP BY p.product_id, p.product_name
ORDER BY total_sales DESC, p.product_id ;