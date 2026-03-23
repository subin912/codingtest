def solution(triangle):
# triangle 자체를 DP 테이블처럼 사용한다.
# 즉 triangle[i][j]의 원래 값에
# "해당 위치까지 도달했을 때의 최대 누적합"을 계속 덮어쓴다

    # 실제 계산은 1번째 줄부터 시작
    for i in range(1, len(triangle)):
		    # i번째 줄에는 원소가 i+1개 있음
		    # i=1 -> 2개, i=2 -> 3개
        for j in range(len(triangle[i])):

            if j == 0:
                # 왼쪽 끝 -> 위에서만 내려옴
                triangle[i][j] += triangle[i-1][j]

            elif j == len(triangle[i]) - 1:
                # 오른쪽 끝 → 왼쪽 위에서만 내려옴
                triangle[i][j] += triangle[i-1][j-1]

            else:
                # 가운데 → 왼쪽 위, 오른쪽 위 중 더 큰 값 선택
                triangle[i][j] += max(
                    triangle[i-1][j-1], 
                    triangle[i-1][j] 
                )


    return max(triangle[-1])
    # 마지막 줄에는
		# "각 위치까지 왔을 때의 최대 누적합"이 저장되어 있음
		# 따라서 마지막 줄에서 가장 큰 값이 전체 최대합