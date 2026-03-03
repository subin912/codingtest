import math

def solution(progresses, speeds):
    # 1. 각 기능이 완료되기까지 걸리는 날짜 계산
    days = []  # 각 기능이 완료되는 데 필요한 날짜를 저장할 리스트
    
    # progresses ,speeds 동시 순회
    for p, s in zip(progresses, speeds):
        remain = 100 - p# 남은 작업량 계산
        # 작업은 하루 단위로 배포되므로 올림 처리
        days.append(math.ceil(remain / s))
    
    # 예: progresses=[93,30,55], speeds=[1,30,5]
    # days = [7, 3, 9]

    
    # 2. 앞에서부터 배포 묶기
    # 핵심 규칙: 뒤 기능이 먼저 끝나도 앞 기능이 끝날 때까지 기다려야 같이 배포됨
    
    answer = []  # 각 배포마다 배포되는 기능 개수 저장
    current = days[0]  # 첫 번째 기능 완료일 기준
    count = 1          # 첫 번째 기능은 일단 1개
    
    # 두 번째 기능부터 순회
    for i in range(1, len(days)):
        
        # 만약 다음 기능 완료일이
        # 현재 배포 기준일보다 작거나 같다면
        # → 같이 배포 가능
        if days[i] <= current:
            count += 1
        
        # 더 오래 걸린다면
        # → 지금까지 묶인 것 먼저 배포
        else:
            answer.append(count)  # 현재 묶음 저장
            current = days[i]     # 새로운 배포 기준일 갱신
            count = 1             # 새로운 묶음 시작
    
    # 마지막 묶음 추가 (반복문 끝난 뒤 남아있는 것)
    answer.append(count)
    
    return answer