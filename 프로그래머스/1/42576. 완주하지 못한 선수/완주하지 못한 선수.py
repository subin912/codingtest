def solution(participant, completion):
    participant.sort() #정렬하면 같은이름끼리 항상 같은 위치에서 비교됨
    completion.sort()
    
    
    for p, c in zip(participant, completion):
        #zip = 짧은 리스트 기준으로 멈춤
        if p != c:
            return p
    return participant[-1] #남는거 하나가 완주못한 선수임