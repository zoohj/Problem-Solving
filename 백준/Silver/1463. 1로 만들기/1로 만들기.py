# https://www.acmicpc.net/problem/1463
# 1463 1로 만들기
# 알고리즘: DP
# 핵심: 점화식 규칙성 찾기, 조건부 갱신

'''
그리디 ❌ → DP ⭕

dp[i] = i를 1로 만드는 최소 연산 횟수
기본: dp[i] = dp[i-1] + 1
조건부 갱신:
i % 2 == 0 → dp[i//2] + 1
i % 3 == 0 → dp[i//3] + 1
'''

import sys
input = sys.stdin.readline

n = int(input()) 

dp = [0]* max(4, (n+1))  

dp[2]=1
dp[3]=1
for i in range(4,n+1):
    dp[i]= dp[i-1] + 1
    if i%3==0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2==0:        
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[n])