def solution(park, routes):
    #1. 그래프, 좌표문제니까
    n,m = len(park), len(park[0])
    #2.방문표시안해도될듯 좌표 찍기
    dx = [-1,1,0,0] #NSWE
    dy = [0,0,-1,1]
    
    #3.수행하기 
    #3-1.(시작 위치 찾기)
    for i in range(n): #세로
        for j in range(m): #가로
            if park[i][j] == 'S':
                x, y = i, j
                
    #3-2. 명령 하나씩 실행
    for route_split in routes:
        op, nt = route_split.split()
        nt = int(nt)
        d = 'NSWE'.index(op) #'NSWE'방향문자
        ddx, ddy = dx[d], dy[d] 

    #3-3. 그림자 출발
        nx, ny = x, y #그림자 출발
        possible = True #일단 갈 수 있다고 가정
    
        #3-4. 좌표 이동시키기
        for _ in range(nt): #0,1,2,~,nt-1까지 돌아 즉 칸 이동하는 거임
            nx, ny = nx + ddx, ny + ddy #한칸 이동
            if not (0 <= nx < n and 0 <= ny < m) or park[nx][ny] == 'X':
                possible = False # 밖이거나 장애물 → 실패
                break
            
        if possible:        #끝까지 갈 수 있을 때만 이동
            x, y = nx, ny
        
    
    return [x,y]