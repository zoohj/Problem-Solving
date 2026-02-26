import math 

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    # y(세로)는 3부터 전체 격자 수의 제곱근까지
    for i in range(3,int(math.sqrt(total))+1):
        if total % i == 0:
            y = i
            x = total // y
            if 2*(x+y)-4 == brown:
                answer = [x, y]
                break
    return answer 

'''
가로(x),세로(y)
brown(테두리) = (가로+세로-1)*2-2 = 2(가로+세로)-4
yellow(중앙) = 가로*세로 - brown
전체 격자 개수 = 가로 * 세로 = brwon+yellow

brown = 2(x+y)-4
yellow = x*y - brown = x*y - (2x+2y-4) = xy - 2x -2y+4

answer.append(x,y)

'''