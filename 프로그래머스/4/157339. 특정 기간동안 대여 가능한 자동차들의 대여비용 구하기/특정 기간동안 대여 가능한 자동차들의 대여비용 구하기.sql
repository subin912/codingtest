-- 코드를 입력하세요
SELECT R.CAR_ID, R.CAR_TYPE, ROUND(DAILY_FEE * 30 * ((100-DISCOUNT_RATE)/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR R JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON R.CAR_TYPE = P.CAR_TYPE
WHERE R.CAR_TYPE IN ('세단', 'SUV') AND P.DURATION_TYPE = '30일 이상' 
        AND R.CAR_ID NOT IN (SELECT CAR_ID 
                            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                            WHERE START_DATE <='2022-11-30' AND END_DATE>='2022-11-01') ## 11월에 대여한 것들 빼는 거 = NOT IN
HAVING FEE BETWEEN 500000 AND 1999999 #WHERE에서는 보통 SELECT에서 만든 별칭(FEE)을 직접 못 쓰기에 having에서 쓴다
ORDER BY FEE DESC, R.CAR_TYPE ASC, R.CAR_ID DESC;

# 대여 시작일이 11/30보다 같거나 이전 OR 대여종료일이 11/1보다 같거나 이후면
# 대여 기간이 11월 구간(11/01~11/30)과 한 번이라도 겹친다는 뜻
## R.CAR_ID NOT IN (겹치는 대여 기록이 있는 CAR_ID들) 
## 즉,11월에 빌려진 적이 있는 차는 제외하고 11월에 빌릴 수 있는 차만 남긴다는 뜻

####################
# SELECT c.car_id, c.car_type, FLOOR(c.daily_fee*30*(1-p.discount_rate/100)) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR c 
#     LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
#     ON c.car_id = h.car_id 
#     AND h.start_date <= '2022-11-30' AND h.end_date >= '2022-11-01'
#     JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p 
#     ON p.car_type = c.car_type
# WHERE 
#     (c.car_type = 'SUV' OR c.car_type = '세단') 
#     AND h.car_id IS NULL 
#     AND ((p.car_type = '세단') OR (p.car_type = 'SUV'))
#     AND (p.duration_type = '30일 이상')
#     AND (c.daily_fee*30*(1-p.discount_rate/100) >= 500000)
#     AND (c.daily_fee*30*(1-p.discount_rate/100) < 2000000)
# ORDER BY FEE DESC, car_type ASC, car_id DESC ;