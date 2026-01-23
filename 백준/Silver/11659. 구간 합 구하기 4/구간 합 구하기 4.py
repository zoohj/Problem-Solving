# 11659 구간 합 구하기 4
# 알고리즘: 누적합
# 핵심: 리스트로 구현하면 시간초과가 나기 때문에 누적합으로 구현

'''
input_data [_,_, ...] data[0]이 첫번째 값
prefix_sum [0,0,0, ... ] => prefix_sum[1]에 1번째까지의 합을 저장
'''

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
input_data= list(map(int,input().split())) 

prefix_sum = [0] * (n + 1)
# 누적합 계산
for i in range(n):
    prefix_sum[i+1] = input_data[i] + prefix_sum[i]

for _ in range(m):
    a, b = map(int,input().split())
    # b까지의 합 - (a-1)까지의 합
    print(prefix_sum[b] - prefix_sum[a-1])

