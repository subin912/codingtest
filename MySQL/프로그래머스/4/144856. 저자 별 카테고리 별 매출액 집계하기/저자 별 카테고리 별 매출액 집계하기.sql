-- 코드를 입력하세요
SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(b.price*s.sales) as TOTAL_SALES
FROM BOOK_SALES s LEFT JOIN BOOK b ON b.BOOK_ID = s.BOOK_ID LEFT JOIN AUTHOR a on a.author_id = b.author_id
Where s.sales_date like "2022-01%"
GROUP BY b.AUTHOR_ID, b.category
ORDER BY AUTHOR_ID asc, category DESC;