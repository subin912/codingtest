def solution(k, dungeons):
    visited = [False]*len(dungeons)
    
    def dfs(curt_k): #현재 피로도로 최대로 몇개 더 갈 수 있는지 반환
        max_cnt = 0 # 더 갈 수 있는 최대 던전 수 
    
        for i in range(len(dungeons)):
            if not visited[i]: 
                need, mnus = dungeons[i]
            
            #현재 피로도 >= 최소필요피로도면 들어갈 수 있다.
                if curt_k >= need: 
                    visited[i] = True
                    count = 1 + dfs(curt_k - mnus) # 하나 갔다 왔으니까 +1
                    max_cnt = max(max_cnt, count) #최대값 갱신하기
                    visited[i] = False # 다시 원상복구 (백트래킹)
                    
        return max_cnt
            
    return dfs(k)
    