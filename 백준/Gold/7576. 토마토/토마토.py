# https://www.acmicpc.net/problem/7576
# 7576 토마토

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = [[0] for _ in range(n)]

for i in range(n):
    box[i] = list(map(int, input().split()))

queue = deque()
zero_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(box) and 0 <= ny < len(box[0]) and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
        elif box[i][j] == 0:
            zero_cnt += 1

if zero_cnt == 0:
    print(0)
else:
    dfs()
    feasibility = True
    max_num = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                feasibility = False
            elif box[i][j] > max_num:
                max_num = box[i][j]
    if not feasibility:
        print(-1)
    else:
        print(max_num - 1)
