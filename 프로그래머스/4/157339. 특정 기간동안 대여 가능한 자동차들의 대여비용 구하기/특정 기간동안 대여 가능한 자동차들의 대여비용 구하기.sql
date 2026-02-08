-- 코드를 입력하세요
SELECT c.car_id, c.car_type, FLOOR(c.daily_fee*30*(1-p.discount_rate/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c 
    LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
    ON c.car_id = h.car_id 
    AND h.start_date <= '2022-11-30' AND h.end_date >= '2022-11-01'
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p 
    ON p.car_type = c.car_type
WHERE 
    (c.car_type = 'SUV' OR c.car_type = '세단') 
    AND h.car_id IS NULL 
    AND ((p.car_type = '세단') OR (p.car_type = 'SUV'))
    AND (p.duration_type = '30일 이상')
    AND (c.daily_fee*30*(1-p.discount_rate/100) >= 500000)
    AND (c.daily_fee*30*(1-p.discount_rate/100) < 2000000)
ORDER BY FEE DESC, car_type ASC, car_id DESC ;