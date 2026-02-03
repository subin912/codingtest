def solution(routes):
    routes.sort(key=lambda x: x[1])
    count = 1
    camera = routes[0][1] # 첫 차량 진출 지점: 카메라 설치
    #print(routes[1][0])
    
    for i in range(1,len(routes)):
        #만약에 처음 나가는 것보다 진입지점이 더 안에 있으면?
        if routes[i][0] > camera:
            count = count + 1
            camera = routes[i][1]

    return count

#count - 몇대 설치했는지
#camera - 지금 어디에설치돼 있는지 