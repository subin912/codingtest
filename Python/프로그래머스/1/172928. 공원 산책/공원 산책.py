def solution(park, routes):
    #좌표 문제, 그래프
    n,m = len(park), len(park[0]) #세로, 가로
    
    #좌표 #북남서동
    move = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)} 
    
    #시작점 찾기
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
                
    #움직임 명령 실행하기 
    for route in routes:
        op, nt = route.split()
        nt = int(nt)
        
    #그림자 수행
        nx, ny = x,y  #그림자 지정하기 (대신할거 적용)
        possible = True
        for i in range(nt):
            nx, ny = nx + move[op][0], ny + move[op][1] #그림자 자기자신에 적용해야함!!
            if not (0<= nx < n and 0 <= ny < m) or (park[nx][ny] == 'X'): #좌표 안에있지 않고, 막히면
                    possible = False
                    break
                    
        if possible == True:
            x,y = nx, ny
                
    return [x,y]