# https://www.acmicpc.net/problem/11659
# 11652 카드
# 알고리즘: 정렬
# 핵심: 너무 어렵게 생각하지말기

'''
[1,1,1,2,2]
'''

import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

# 1. 정렬 (O(N log N))
cards.sort()

res = cards[0] # 맨앞부터 시작
max_cnt = 1
curr_cnt = 1

for i in range(1, n):
    if cards[i] == cards[i-1]:
        curr_cnt += 1
    else:
        curr_cnt = 1
    
    # 더 많이 나타난 숫자로 갱신 (정렬되어 있어 작은 숫자가 먼저 나옴)
    if curr_cnt > max_cnt:
        max_cnt = curr_cnt
        res = cards[i]

print(res)