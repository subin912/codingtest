-- 코드를 입력하세요
SELECT history_id, car_id, start_date, end_date, 
    IF(DATEDIFF(end_date, start_date) +1 >= 30,'장기 대여','단기 대여') AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(start_date) = 9
ORDER BY HISTORY_ID desc;