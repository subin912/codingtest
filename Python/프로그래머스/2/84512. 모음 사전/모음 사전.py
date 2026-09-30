def solution(word):
    list = ['A','E','I','O','U']
    
    words = []
    
    #3. dfs껍데기 정의
    ## 길이가 6보다 크면 안되고
    ## 붙여야돼
    ## word에도 저장해야해
    def dfs(current):
        if len(current) > 5:
            return
        if current: #추가하기
            words.append(current)
            
        for v in list:
            dfs(current + v)
    
    
    #4.dfs 실행
    dfs("")
    
    return words.index(word)+1