def solution(n, wires):
    #1. graph
    graph = [[] for _ in range(n+1)]
    
    #1-1.값 채우기
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    #2. visited 배열 준비 - 생략 (반복해야하기 때문)
    answer = n
    
    #3.dfs - 함수
    def dfs(v,cut_a,cut_b): #현재
        count = 1 #나자신
        visited[v] = True
        
        for nxt in graph[v]: #이웃돌릴거야
            if (v,nxt) == (cut_a,cut_b) or (v,nxt) == (cut_b,cut_a):
                continue #끊기는 부분 빼고 세어야하니까
            
            if not visited[nxt]: #방문안한곳이면
                count = count + dfs(nxt,cut_a,cut_b)
        return count
        
        
    #4. 실전 자르기 ##반복해야됨
    for a,b in wires:
        visited= [False]*(n+1)
        count = dfs(a,a,b) #끊을 전선은 a,b임!
        
        answer = min(answer,abs(count-(n-count)))
    
    return answer