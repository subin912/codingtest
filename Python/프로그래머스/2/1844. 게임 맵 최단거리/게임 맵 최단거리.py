from collections import deque

def solution(maps):
    #최솟값 return - bfs
    #1.좌표 (그래프안해도도됨)
    n, m = len(maps), len(maps[0]) #세로,가로
    #1-1.좌표 채우기
    
    #2.방문표시/ 이동해야지
    dist = [[-1]*m for i in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    #3.bfs 시작
    #3-1. 시작전 준비
    q = deque([(0,0)])
    dist[0][0] = 1
    
    #3-2. q반복하기 빌때까지
    #움직이기 #n,m까지 가야함
    while q:
        x,y = q.popleft() #3-3.하나빼기
        
        for i in range(4): #3-4.뺀거 방향전환하기 (시험시작)
            nx, ny = x+dx[i], y+dy[i]
            
            if (0<=nx<n and 0<=ny<m) and maps[nx][ny] == 1 and dist[nx][ny] == -1: #maps안이고, maps의 갈수있는길(=1)이면고, 아직 안가본길 
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    
    return dist[n-1][m-1]