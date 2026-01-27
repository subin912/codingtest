# 큰수 남기기가 아닌 작은 숫자를 빼기
#삭제하기 즉 뺄거 고르기!작은거 빼는거! : 스택 - 후입선출 

def solution(number, k):
    stack = []
    
    for i in number:
        #뒤에서 더 큰애 있으면 앞 숫자 제거
        while stack and (k > 0) and stack[-1] < i: #stack은 비어있지않으면 true가 됨!!
            stack.pop()
            k = k-1
        
        # 숫자를 스택에 쌓음
        stack.append(i)
        
    # 아직 k가 남아있다면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)