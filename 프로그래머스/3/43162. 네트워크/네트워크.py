def solution(n, computers):
    network = 0
    visited = [False] * n # 1. 모든 컴퓨터의 방문 여부를 체크할 리스트
    
    # 2. 0번부터 n-1번 컴퓨터까지 하나씩 순회함
    for i in range(n): # '총괄 매니저' for문
        if not visited[i]: # 아직 아무도 안 가본 새로운 땅(컴퓨터)을 발견했다면?
            network = network +1 # 네트워크 개수 추가 ("새 네트워크 하나 찾았다!" 하고 카운트)
            # 3. 스택(바구니)에 시작 컴터 넣기
            stack = [i]
            
            # 4. 스택이 빌 때까지 연결된 모든 컴터 찾아다님
            while stack: #(이 안에서는 이미 찾은 네트워크의 '내부'를 샅샅이 뒤지는 중...)
                current = stack.pop() # 가장 최근에 넣은 컴퓨터 꺼내기
                if not visited[current]:
                    visited[current] = True # 방문도장 찍기
                    
                    # 5. 현재 컴퓨터(current)와 연결된 다른 컴퓨터(j)를 찾습니다.
                    for j in range(n):
                        # 연결되어 있고(1), 아직 방문 전이라면 스택에 추가!
                        if computers[current][j] == 1 and not visited[j]:
                            stack.append(j)
                            
    return network