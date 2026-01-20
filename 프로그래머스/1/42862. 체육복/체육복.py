# 전체 학생수 n
# lost : 체육복 잃어버린 학생 번호 목록
# reserve : 여벌 체육복 가진 학생 번호 목록

def solution(n, lost, reserve):
    answer = 0
    #1. set으로 다시 저장하기
    lost = set(lost)
    reserve = set(reserve)
    
    #2. 교집합(잃어버렸는데 여벌도 있는 학생) 먼저 제거 
    if lost & reserve:
        common = lost & reserve #교집합은 한번 변수에 저장해두고 양쪽에서 제거해야함
        lost = lost - common
        reserve = reserve - common
     #3. 이제 빌려주기 (빌려줄 수 있는지 확인)
    for i in list(lost): #반복 중 set 변경하면 오류나기에 list로 방지 
        if i - 1 in reserve: # 앞번호 학생이 여벌 있으면 빌림
            reserve.remove(i-1) # 여벌 사용하기 
            lost.remove(i) # 체육복 문제 해결
            
        elif i + 1 in reserve: # 앞번호 x, 뒷번호 학생 여벌 있으면 빌림
            reserve.remove(i+1) # 여벌 사용하기 
            lost.remove(i) # 체육복 문제 해결
            
        else: # 앞/뒤 모두 여벌이 없으면 아무것도 못 함  
            pass
    # 체육복 입을 수 있는 학생 수 
    return n - len(lost)


#다른 풀이 
def solution(n, lost, reserve):
    #교집합 제거 (리스트 컴프리헨션) - 잃어버렸지만 여벌도 있는 학생 제거 
    _reserve = [r for r in reserve if r not in lost] 
    _lost = [l for l in lost if l not in reserve]
    # 여벌 가진 사람 기준으로 빌려주기 
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)
