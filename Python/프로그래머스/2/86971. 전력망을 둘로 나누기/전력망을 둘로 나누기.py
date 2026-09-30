def solution(n, wires):
    #1. 그래프 만들기
    graph = [[] for i in range(n+1)]
    
    #1-1. 정보 채우기
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)

    #3. dfs 함수 정의 시작 #한쪽 개수세주는것
    def dfs(v, visited, cut_a, cut_b): #현재 위치, 방문?, 끊을거1,2
        visited[v] = True  #되돌리지 않아서 true만 함
        count = 1 # 나 자신 1개
        
        for nxt in graph[v]: #옆에 붙은 송전탑으로 하나씩 고고
            if(v,nxt) == (cut_a,cut_b) or (v, nxt) == (cut_b, cut_a): #2랑 엮인애가 [1,3,5]라면
                continue # 끊긴 전선이면 건너뜀 #3이 끊겨있으면 3만 건너뛰고 나머지 세어야하니까
            if not visited[nxt]: #[3,5]
                count = count + dfs(nxt, visited, cut_a, cut_b)   # 그쪽에서 센 개수를 더함
        return count
    
        
    #3-3. 전선 하나씩 끊어보기
    answer = n  # 최솟값을 찾으니까 큰 값으로 시작 #두쪽 차이가 n보다 클수없으니까 //n으로 시작하면 첫 비교에서 무조건 바뀌어. 0으로 시작하면 min(0, 무엇)이 항상 0이 돼서 틀려.
    for a,b in wires: #자르러 간다  # 전선 [a, b]를 끊는다고 가정
        visited = [False]*(n+1)   # 끊을 때마다 새 체크리스트. 이전 전선을 끊었을 때 체크한 기록이 남아 있으면, 이번에 셀 때 방해가 돼.
        count = dfs(a, visited, a,b) # a 쪽 덩어리 크기 #a에서 출발해서, a-b 전선은 끊겼다고 치고, 연결된 송전탑을 세어줘
        answer = min(answer, abs(count - (n - count))) #cnt: a 쪽 송전탑 수 #n - cnt: 나머지 전부니까 반대쪽 송전탑 수
        
    return answer