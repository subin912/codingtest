#2:25-37분 #최솟값 return - 빨리가는거최대로
from collections import deque
def solution(maps):
    answer = 0
    #1.좌표
    n,m = len(maps), len(maps[0])
    #1-1.채우기  X 채워져있음
    #2.visited/disit
    dist = [[-1]*m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    #3.bfs
    #3-1.시작점 넣기
    dist[0][0] =1 #적고
    q = deque([(0,0)]) #넣기 #튜플로!!
    
    #3-2.큐가 빌때까지 반복
    while q:
        #큐 하나씩 꺼내기 #3-3
        x,y = q.popleft()
        #3-4. 상하좌우 이동해주기
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
        
            #3-5. 조건 파악 찾기
            if (0<=nx<n and 0<=ny<m) and maps[nx][ny] == 1 and dist[nx][ny] == -1: #범위 안에 드는지,벽이아닌지,방문체크 안한 곳인지
                dist[nx][ny] = dist[x][y] + 1#적고
                q.append((nx,ny)) #넣고
                
    return dist[n-1][m-1]