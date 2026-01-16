#1913 달팽이
'''
n**2
달팽이 반대로 이동 (아래,오른쪽, 위, 왼쪽)

'''

import sys
input = sys.stdin.readline


n = int(input())
target = int(input())

# 변수 초기화
x=0
y=0
board = [[0]*n for _ in range(n)]
target_x, target_y = 0, 0
if n**2 == target:
    target_x, target_y = x,y

# 아래, 오른쪽, 위, 아래
dx = [1, 0,-1, 0]
dy = [0, 1, 0,-1]

dist_idx=0
board[0][0]=n**2                # 시작점 초기화
for num in range(n**2-1, 0, -1):

    # 아래, 오른쪽, 위, 아래
    dx = [1, 0,-1, 0]
    dy = [0, 1, 0,-1]

    # 다음 위치 계산
    nx = x + dx[dist_idx]
    ny = y + dy[dist_idx]
    
    # 범위를 벗어났거나 이미 숫자가 있다면 방향 전환
    if not (0<=nx<n and 0<=ny<n) or board[nx][ny] != 0 : 
        dist_idx = (dist_idx+1)%4
        nx = x + dx[dist_idx]
        ny = y + dy[dist_idx]

    x, y = nx, ny
    board[x][y] = num
    # print(x,y,board[x][y])

    # 찾고자하는 숫자 위치 저장
    if num == target:
        target_x = x
        target_y = y

for row in board:
    print(*row)

print(target_x+1,target_y+1)
