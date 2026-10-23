#최대한 빨리 - bfs/간거 세야해 하나더 좌표 만들어야함
from collections import deque
def solution(maps):
    answer = 0
    #1.그래프(격자형)
    n,m = len(maps), len(maps[0])
    #1-1. 채우기생략
    
    #2.좌표/ dist - 이웃 따로 안적혀있으니까
    dist = [[-1]*m for _ in range(n)] #n줄에 m칸
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    #3. bfs
    #3-1. 시작점 넣기 #문제그림에선 (1,1)에서 출발해도 python 리스트에서는 0부터 출발, 그리고 큐에는 좌표를 튜플 하나로 넣어야함.
    q = deque([(0,0)])
    dist[0][0] = 1 #시작 칸도 1칸으로 세기 때문.
    
    #3-2.q가 빌 때까지 반복
    while q:
        x, y = q.popleft() # 3-3. q하나씩 꺼내기
        for i in range(4):
            nx, ny = x + dx[i], y+ dy[i] #그림자로 가야됨
            
            #3-4. 조건파악
            if ((0<=nx<n) and (0<=ny<m)) and maps[nx][ny] == 1 and dist[nx][ny] == -1: #가능한 조건,'-1'안됨. 문자 '-1'이라 영원히 거짓
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny)) #넣기
    
    return dist[n-1][m-1]