import math

def solution(fees, records): #입력: 요금표, 차량기록
    
    #딕셔너리!!
    in_car = {} #들어온 차
    total = {} #누적
    
    #1. 차량별 기록분류하기 (3개쪼개기)
    for i in records: #기록 꺼내기
        t, car, memo = i.split(' ')
        h,m = map(int, t.split(':'))
        time = h*60 + m
        
        # 1-1.in, out 구분
        if memo == 'IN':
            in_car[car] = time #들어온 시각 적기만 하면됨. get + 누적이 필요함
        else: #out이면 전에서 빼야됨
            total[car] = total.get(car,0) + time - in_car[car]
            del in_car[car]
        
    for car, t in in_car.items(): #기록에 남아있다면 시간넣어주기
            total[car] = total.get(car, 0) + (23*60+59) - t
        
    
    
    #2. 계산하기
    answer = []
    
    for car in sorted(total): #차량 번호 작은것부터 정렬하기
        #값 계산
        if total[car] <= fees[0]: #기본시간 
            answer.append(fees[1])
        else: #기본시간 넘는다면
            answer.append(math.ceil((total[car]-fees[0])/fees[2])*fees[3] + fees[1] )
            
    return answer