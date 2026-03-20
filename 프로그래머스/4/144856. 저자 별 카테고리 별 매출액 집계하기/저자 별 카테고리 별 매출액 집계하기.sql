-- 코드를 입력하세요
SELECT a.author_id, a.author_name, b.category, sum(b.price*bs.sales) as total_sales
FROM BOOK b 
JOIN BOOK_SALES bs ON b.book_id = bs.book_id
JOIN AUTHOR a ON a.author_id = b.author_id
WHERE bs.sales_date >= '2022-01-01'AND bs.sales_date <= '2022-01-31'
GROUP BY a.author_id, b.category
ORDER BY a.author_id, b.category desc;

