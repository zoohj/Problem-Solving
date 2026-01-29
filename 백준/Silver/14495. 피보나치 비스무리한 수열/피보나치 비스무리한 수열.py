# https://www.acmicpc.net/problem/14495
# 14495 피보나치 비스무리한 수열
# 알고리즘: dp
# 핵심: 이전 값을 이용

'''
f(n) = f(n-1) + f(n-3)
f(1) = f(2) = f(3) = 1
'''

import sys
input = sys.stdin.readline

n = int(input()) 
dp = [0]* (max(4,n+1))

dp[1]=1
dp[2]=1
dp[3]=1

for i  in range(4, n+1):
    dp[i] = dp[i-3]+dp[i-1]

print(dp[n])

