-- 코드를 입력하세요
SELECT DISTINCT h.car_id 
FROM CAR_RENTAL_COMPANY_CAR c RIGHT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON c.car_id = h.car_id
WHERE c.car_type = '세단' AND MONTH(h.start_date) = '10' 
ORDER BY h.car_id DESC;