# https://www.acmicpc.net/problem/2143
# 2143 두 배열의 합
# 알고리즘: 누적합, 딕셔너리

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


a_prefix_sum = {}
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        if temp not in a_prefix_sum:
            a_prefix_sum[temp] = 1
        else:
            a_prefix_sum[temp] += 1

b_prefix_sum = {}
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        if temp not in b_prefix_sum:
            b_prefix_sum[temp] = 1
        else:
            b_prefix_sum[temp] += 1

answer = 0
for a_sum, a_count in a_prefix_sum.items():
    need = t - a_sum
    if need in b_prefix_sum:
        answer += b_prefix_sum[need] * a_count
print(answer)