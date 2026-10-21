-- 코드를 입력하세요
SELECT CAR_ID, round(avg(datediff(end_date,start_date)+1),1) as AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY car_id
HAVING round(avg(datediff(end_date,start_date)+1),1) > 7 
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;