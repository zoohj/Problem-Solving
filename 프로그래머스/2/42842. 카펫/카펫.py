import math

def solution(brown, yellow):

    # 1. 전체 격자 수 계산
    total = brown + yellow
    answer = []

    # 2. 세로(y)는 최소 3부터 전체 넓이의 제곱근까지 탐색
    # 가로(x) >= 세로(y) 조건을 만족하기 위함
    for y in range(3, int(math.sqrt(total)) + 1):
        # 3. total의 약수인 경우만 체크
        if total % y == 0:
            x = total // y  # 가로 길이 계산
            
            # 4. ⭐️ 수식 검증 
            # brown = 2*(가로+세로-1)-2 = 2(가로+세로)-4
            if 2*(x+y)-4 == brown:
                answer = [x, y]
                break
                
    return answer