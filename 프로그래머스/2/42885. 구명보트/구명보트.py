from collections import deque

def solution(people, limit):
    answer = 0
    
    # 1. 몸무게 오름차순 정렬
    people.sort()
    
    # 2. 리스트를 deque로 변환
    people = deque(people)
    
    # 3. 사람이 남아 있는 동안 반복
    while people:
        # case 1: 한 명만 남았을 때
        if len(people) == 1:
            people.pop()       # 마지막 한 명 태우고
            answer += 1        # 보트 1개 사용
        else:
            # 가장 가벼운 사람 + 가장 무거운 사람
            if people[0] + people[-1] <= limit:
                # 같이 탈 수 있으면 둘 다 태우기
                people.popleft()   # 가장 가벼운 사람 보트 탑승
                people.pop()       # 가장 무거운 사람 보트 탑승
                answer += 1
            else:
                # 둘이 같이 못 타면, 무거운 사람 혼자 보트 타야 함
                people.pop()       # 가장 무거운 사람만 태움
                answer += 1
    
    return answer
