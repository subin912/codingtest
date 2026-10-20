def solution(s): # 결과는 숫자로!!
    answer = ''
    mop = ('zero','one','two','three','four','five','six','seven', 'eight','nine')
    for i in mop:
        s = s.replace(i, str(mop.index(i)))
        
    answer = int(s)
    return answer