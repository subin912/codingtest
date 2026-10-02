from collections import deque

def solution(maps):
    #1.좌표지도
    n,m = len(maps), len(maps[0])
    
    #2.
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    dist = [[-1]*m for _ in range(n)]
    
    #3.bfs
    #3-1.시작점 넣기
    q = deque([(0,0)])
    dist[0][0] = 1
    
    #3-2.bfs가동
    while q:
        x,y = q.popleft() #3-3.하나씩 빼기
        for i in range(4): #3-4. 상하좌우
            nx,ny = x +dx[i], y+dy[i]
        
            if (0<=nx<n and 0<=ny<m) and dist[nx][ny]==-1 and maps[nx][ny]==1:
                dist[nx][ny] = dist[x][y] +1 #거리기록
                q.append((nx,ny)) #새로찾은칸을 꺼내지않고 넣어야지
    
        
    return dist[n-1][m-1]