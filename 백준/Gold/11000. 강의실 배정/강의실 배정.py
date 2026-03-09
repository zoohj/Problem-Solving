# https://www.acmicpc.net/problem/11000
# 11000 강의실 배정
# 알고리즘: 정렬, 우선순위 큐
# 핵심: heap의 크기가 동시에 돌아가고있는 강의실 수

import sys
import heapq

input = sys.stdin.readline
n = int(input())
time_table = []

for _ in range(n):
    s, e = map(int, input().split())
    time_table.append((s, e))

time_table.sort()  # 시작시간 기준으로 정렬

heap = []
# 첫 강의의 종료시간을 heap에 저장 (강의실 1개 사용 시작)
heapq.heappush(heap, time_table[0][1])

for i in range(1, n):
    # 현재 강의 시작시간 >= 가장 빨리 끝나는 강의
    # → 해당 강의실 재사용 가능
    if time_table[i][0] >= heap[0]:
        heapq.heappop(heap)  # 끝난 강의 제거 (강의실 비움)

    # 현재 강의가 강의실 하나를 사용하므로 종료시간 추가
    heapq.heappush(heap, time_table[i][1])

# heap에는 현재 동시에 진행중인 강의들의 종료시간이 들어있음
# heap 길이 = 동시에 필요한 강의실 수
print(len(heap))
