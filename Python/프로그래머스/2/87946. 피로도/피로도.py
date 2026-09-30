def solution(k, dungeons):
    #1. visited 배열 준비
    visited = [False]*len(dungeons)
    
    #2. dfs 함수 정의 (아직 실행 안됨)
    def dfs(curt_k): #매번 바뀌어야할 것
        max_cnt = 0 # 초기 정답 셋팅
        #던전 돌기 시작
        for i in range(len(dungeons)):
            if not visited[i]: #안가봤으면 
                need, mnus = dungeons[i] #가보게 부여
                
                #근데 들어갈 수 있니? 현재 피로도 >= 최소필요피로도면 들어갈 수 있다.
                if need <= curt_k: #피로도 들어갈 수 있으면
                    visited[i] = True
                    count = 1 + dfs(curt_k- mnus)
                    max_cnt = max(max_cnt, count)
                    visited[i] = False #다시 원상복구(백트래킹)
                    
        return max_cnt     
    
    return dfs(k) #③여기서 처음 실행→결과를 그대로 정답으로 반환