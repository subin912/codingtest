# 큰수 남기기가 아닌 작은 숫자를 빼기
#삭제하기 즉 뺄거 고르기!작은거 빼는거! : 스택 - 후입선출 

def solution(number, k):
    stack = []
    
    for i in number:
        #뒤에서 더 큰애 있으면 앞 숫자 제거
        while stack and (k > 0) and stack[-1] < i: #조건 충족할 때까지 못나가 
            #stack은 비어있지않으면 true가 됨!! + k =0 되면 쫓아낼수없어서 그냥 append.
            #stack[-1] < i : 내 앞에 써진 숫자가 나보다 작은가 -> 작으면 pop 실행.
            #새로 들어온 숫자가 stack 가장 최근숫자보다 클때 기존꺼들 제거 - 후입선출
            #ex)1924,2,94
            stack.pop()
            k = k-1
        
        # 숫자를 스택에 쌓음
        stack.append(i)
        
    # 아직 k가 남아있다면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)


#내 뒤에 나보다 키(숫자)가 큰 친구가 오면, 나는 줄에서 빠져야 해!" (단, 기회는 딱 k번뿐이야!)
#뒤에 나보다 큰 숫자가 기다리고 있다면, 내가 비켜줘야 전체 숫자가 커진다
