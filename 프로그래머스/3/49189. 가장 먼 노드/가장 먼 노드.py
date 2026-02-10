from collections import deque

def solution(n, edge):
    # 1. 인접 리스트 생성 (그래프 만들기)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 2. 거리 저장용 리스트 (아직 방문하지 않은 곳은 -1)
    distances = [-1] * (n + 1)
    distances[1] = 0 # 1번 노드는 시작점이니까 거리 0
    
    # 3. BFS 탐색
    queue = deque() #deque([1]) append 안하고 이렇게 해도됨.
    queue.append(1)
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1: # 아직 방문하지 않았다면
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    # 4. 최대 거리 찾기 및 개수 반환
    max_dist = max(distances)
    return distances.count(max_dist)