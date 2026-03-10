# https://www.acmicpc.net/problem/1931
# 1931 회의실 배정
# 알고리즘: 그리디
# 핵심: 종료시간 기준 정렬 후 가능한 회의 선택

import sys

input = sys.stdin.readline
n = int(input())
time_table = []

for _ in range(n):
    s, e = map(int, input().split())
    time_table.append((s, e))

# 종료시간 기준 정렬 (같으면 시작시간 기준)
# 가장 빨리 끝나는 회의부터 선택하기 위해
time_table.sort(key=lambda x: (x[1], x[0]))

end = 0  # 현재 회의실이 비는 시간
count = 0  # 선택한 회의 개수

for s, e in time_table:
    # 현재 회의 시작시간이 이전 회의 종료시간 이후라면
    # 회의실 사용 가능 (겹치지 않음)
    if s >= end:
        end = e  # 회의실이 다음에 비는 시간 갱신
        count += 1

print(count)
