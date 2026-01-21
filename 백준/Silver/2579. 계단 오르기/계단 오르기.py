#2579 계단 오르기
'''
계단의 최댓값

dp[i] i번째 계단을 꼭 밟았다고 할 때, 최댓값
1. (i-1) 계단 밟은 경우 dp[i-3] + stairs[i-1]+stairs[i]
2. (i-2) 계단 안밟 경우 dp[i-2] + stairs[i]
'''

import sys
input = sys.stdin.readline

n = int(input()) #계단 개수

stairs = [0]*(n+1)
for i in range(1, n+1):
    stairs[i] = int(input())

dp = [0]*301

if n >= 1:
    dp[1]= stairs[1]
if n >= 2:
    dp[2]= stairs[1]+stairs[2]
if n>=3:
    dp[3]= max(stairs[2]+stairs[3], stairs[1]+stairs[3])

for i in range(4,n+1):
    dp[i]=max(dp[i-3] + stairs[i-1]+stairs[i], dp[i-2] +stairs[i])

print(dp[n])