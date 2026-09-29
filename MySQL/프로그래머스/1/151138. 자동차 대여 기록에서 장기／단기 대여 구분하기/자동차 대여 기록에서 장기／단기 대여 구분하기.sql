-- 코드를 입력하세요
SELECT history_id, car_id, 
    date_format(start_date,"%Y-%m-%d") as start_date, end_date, 
    CASE WHEN DATEDIFF(end_date, start_date) +1 >= 30 THEN '장기 대여'
    ELSE '단기 대여'END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(start_date) = 9
ORDER BY HISTORY_ID desc;