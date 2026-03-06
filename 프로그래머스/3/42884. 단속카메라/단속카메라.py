def solution(routes):
    #1
    #routes.sort() #저장안해도 바로 수정됨
    #print(sorted(routes)) - 틀린거
    routes.sort(key= lambda x:x[1])
    #routes(lambda(key = x:x[i][1]) - 틀린거
    
    # 초기값은 밖에두기 고정 (for문 안에넣으면 계속 초기화됨)
    carmera = routes[0][1] 
    answer = 1
    
    #2
    for i in range(1,len(routes)):
        if carmera < routes[i][0]:
            carmera = routes[i][1]
            answer += 1
    return answer

#0.이해하기 (들어갈때3 vs 나올때2)
#1.일단 정렬 - 2번째가 작은애들부터
#2. for문 
# ##맨처음 두번째값을 카메라에저장
# carmer = routes[0][0]
# answer = 1
# ##if carmera < routes[i][0]
#     carmera = routes[i][1]
#     answer += 1
#     return anwer