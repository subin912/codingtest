def solution(tickets):
    # 1. 방문저장
    tickets.sort() #알파벳 순서가 빠른 경로를 먼저 찾기 위해 정렬

    visited = [False] * len(tickets) # 각 티켓 사용 여부 저장
    answer = [] # 완성된 경로들 저장

    #2. dfs함수
    def dfs(airport, route, count):
            # airport : 현재 공항
            # route   : 지금까지 만든 경로
            # count   : 사용한 티켓 개수

        # 티켓을 전부 사용했다면 완성된 경로이므로 저장
        if count == len(tickets):
            answer.append(route)
            return

        #3. for문으로, 모든 티켓을 하나씩 확인
        for i in range(len(tickets)):
            start, end = tickets[i]

            # 현재 공항에서 출발 가능하고, 아직 사용하지 않은 티켓이면
            if start == airport and not visited[i]:
                visited[i] = True # 이 티켓 사용 처리
                dfs(end, route + [end], count + 1) # 다음 공항으로 이동
                visited[i] = False # 다른 경우도 탐색해야 하므로 다시 사용 취소

    # 항상 ICN에서 출발
    dfs("ICN", ["ICN"], 0)

    # 정렬했기 때문에 가장 먼저 찾은 경로가 정답
    return answer[0]