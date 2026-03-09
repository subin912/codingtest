def solution(n, computers):
    # 1. 방문 체크 리스트 만들기
    # 이미 확인한 컴퓨터는 다시 보지 않기 위해 
    visited = [False]*n
    network = 0 # 네트워크 개수 
    
    # 2. dfs 함수 만들기 (친구의 친구 계속 찾기)
    def dfs(i): #한 컴퓨터에서 시작해서 연결된 친구들을 전부 찾기
        visited[i] = True # 현재 컴퓨터를 확인했다고 표시
        
        # 모든 컴퓨터 하나씩 확인 
        for j in range(n):
            
            # i번 컴퓨터와 j번 컴퓨터가 연결되어 있고
            # 아직 확인하지 않은 컴퓨터라면
            if computers[i][j] == 1 and not visited[j]: 
                dfs(j) # 그 컴퓨터에서도 다시 친구들을 찾기
    
    # 3. 네트워크 개수 세기 : 모든 컴퓨터를 하나씩 확인
    for i in range(n):
        # 아직 확인 안한 컴퓨터라면
        if not visited[i]:
            dfs(i) # 그 컴퓨터에서 시작해서 연결된 컴퓨터 친구들 전부 찾기
            network += 1 #네트워크 하나 발견 
            
    # 총 네트워크 개수 반환
    return network


# #1. 노드 상태 = 현재 인덱스 
# #2. 방문 처리 필요함
# visited = [False]*n
# #3. 다음 상태 찾기 
# for next on visited[v]:
# #4. 종료조건
# #5. DFS 호출
