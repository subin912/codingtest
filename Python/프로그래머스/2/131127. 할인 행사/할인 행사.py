def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        ok = True #조건을 만족할때만 true준다
        window = discount[i:i+10]
        
        for j in range(len(want)):
            if window.count(want[j]) < number[j]:
                ok = False
        if ok:
            answer += 1
        
    return answer