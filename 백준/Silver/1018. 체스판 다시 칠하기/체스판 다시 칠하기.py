#1018 체스판 다시 칠하기
'''
MxN 크기의 보드 -> 보드를 잘라서 8*8 체스판
다시 칠해야하는 정사각형의 최소 개수
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 8*8로 해놓고 바꿔야하는 개수 찾고 미니멈 개수 찾자
# 체스판 색 행번호 + 열번호가 홀수면, 같은 색깔 [0][1] [1][0]

originalBoard = []
for i in range(n):
    set = list(input().rstrip())
    originalBoard.append(set)

result = []

for i in range(0, n-8+1):
    for j in range(0, m-8+1):
        draw_W = 0
        draw_B = 0
        # 8*8로 나눈 후 2가지 조건을
        for r in range(i, i+8):
            for c in range(j, j+8):
                # 합이 짝수인 칸
                if (r+c) % 2 == 0:
                    # 시작이 하얀색인 체스판
                    if originalBoard[r][c] != "W":
                        draw_W += 1
                    # 시작이 검은색인 체스판
                    if originalBoard[r][c] != "B":
                        draw_B += 1
                # 합이 홀수인 칸
                else:
                    # 시작이 하얀색인 체스판
                    if originalBoard[r][c] != "B":
                        draw_W += 1
                    # 시작이 검은색인 체스판  
                    if originalBoard[r][c] != "W":
                        draw_B += 1
        # 더 작은 값 넣기
        result.append(draw_W if draw_W<=draw_B else draw_B)

print(min(result))
