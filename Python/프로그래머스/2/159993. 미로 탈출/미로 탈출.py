#최소시간 return -bfs
from collections import deque
def solution(maps):
    #1.좌표지도
    n,m = len(maps), len(maps[0])
    #1-1 좌표 채우기 - 지도 줫음
    # 시작점, 레버 찾기 - 시작점,레버 ~ 다 찾아야함
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i,j
            elif maps[i][j] == 'L':
                lx, ly = i,j
            elif maps[i][j] == 'E':
                ex, ey = i,j
    #bfs 함수 (2번 반복할거 출발 -> 도착거리)
    def bfs(x0,y0,x1,y1):
        #2.visited/dist
        dist = [[-1]*m for _ in range(n)]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        #3.bfs
        #3-1. 시작점 넣기
        dist[x0][y0] = 0 #적고
        q= deque([(x0,y0)])

        while q:#3-2.q가 빌때까지
            x,y = q.popleft() #3-3.하나씩 빼기

            #3-4. 상하좌우 반복
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                #3-5.조건확인
                if (0<=nx<n and 0<=ny<m):
                    if maps[nx][ny] != 'X' and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1 #적고
                        q.append((nx,ny))
        return dist[x1][y1]
    
    # S->L, L->E
    a = bfs(sx,sy,lx,ly)
    b = bfs(lx,ly,ex,ey)
    if a == -1 or b == -1:
        return -1
    return a + b