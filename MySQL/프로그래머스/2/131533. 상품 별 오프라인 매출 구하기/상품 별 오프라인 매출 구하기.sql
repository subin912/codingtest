-- 코드를 입력하세요
SELECT PRODUCT_CODE ,(price * off_amount) as SALES
FROM PRODUCT p JOIN (
    SELECT product_id, sum(sales_amount) as off_amount
    FROM OFFLINE_SALE
    GROUP BY product_id
    ) o ON p.product_id = o.product_id
ORDER BY (price * off_amount) DESC, PRODUCT_CODE ASC;