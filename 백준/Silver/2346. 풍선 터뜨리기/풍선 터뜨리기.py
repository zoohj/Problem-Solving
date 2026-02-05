# https://www.acmicpc.net/problem/2346
# 2346 풍선 터뜨리기
# 알고리즘: deque
# 핵심: rotate 함수 이동 방향


import sys
from collections import deque

input = sys.stdin.readline


t = int(input())
ballon = map(int, input().split())
ans = []
que = deque((i, v) for i, v in enumerate(ballon))

while que:
    distance = que[0][1]
    ans.append(que[0][0] + 1)
    que.popleft()
    if distance > 0:
        que.rotate(-(distance - 1))
    else:
        que.rotate(-distance)

print(*ans)
