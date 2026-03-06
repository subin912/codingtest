##### 3.6 푼거
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




######################################### 전에 푼거
#단속카메라 : 카메라를  최소개수를 설치해서, 모든 차를 한번 이상 찍기
#→ 가장 빨리 고속도로에서 나가는 차부터 처리하자!
#→ 빨리 나가는 차 놓치면 다시 못찍음!

def solution(routes):
    routes.sort(key=lambda x: x[1])  # 나가는 지점 기준 오름차순 정렬
		# 정렬전 :  [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
		# 정렬후 :  [[-18, -13], [-14, -5], [-5, -3], [-20, 15]] # 나가는 차 기준(x[1] 기준 정렬)
		
    count = 1
    camera = routes[0][1]  # 첫 차 나가는 지점에 카메라 설치

    for i in range(1, len(routes)):
        # 이 차가 기존 카메라에 안 찍히면
        if routes[i][0] > camera: #즉 이 카메라보다 더 뒤쪽에 진입했으면 안찍혀
            count += 1
            camera = routes[i][1]  # 새 카메라를 이 차 나가는 지점에 설치

    return count

#count - 몇대 설치했는지
#camera - 지금 어디에설치돼 있는지 


(거리/지점)  -20  -18  -14  -13  -10   -5   -3    0   ...   15
              |    |    |    |    |    |    |    |         |
A차 [-18,-13]      [=========]
B차 [-14, -5]           [==============]
C차 [-5, -3]                           [====]
D차 [-20, 15] [===========================================]

카메라 설치 위치:            📸(-13)       📸(-3)
