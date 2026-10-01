from collections import deque

def solution(maps):
    #1.그래프 만들기
    n, m = len(maps), len(maps[0])
    #1-1.값 채우기
    dx = [-1,1,0,0] #상하좌우
    dy = [0,0,-1,1] 
    
    #2. 방문체크준비 visited
    dist = [[-1]*m for _ in range(n)]
    
    #3.bfs
    #3-1. 시작 전 준비
    q = deque([(0,0)]) # []안에 넣어야 좌표로 들어감.안그러면 따로들어감
    dist[0][0] = 1 #시작점 체크
    
    #큐 빌때까지 시작
    while q:
        x,y = q.popleft() #하나씩꺼내기 
        
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < n and 0<= ny < m: #지도 안이고
                if maps[nx][ny] == 1 and dist[nx][ny] == -1: #벽 아니고, 방문안한곳이면 가
                    dist[nx][ny] = dist[x][y] + 1 #거리 +1 해주기
                    q.append((nx,ny))
    
    return dist[n-1][m-1]