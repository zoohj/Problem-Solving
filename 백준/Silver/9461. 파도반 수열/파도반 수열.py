# https://www.acmicpc.net/problem/9461
# 9461 파도반 수열
# 알고리즘: 다이나믹 프로그래밍 (DP)
# 핵심: 새로 추가되는 정삼각형의 한 변의 길이는 이전 단계들의 조합으로 결정

import sys
input = sys.stdin.readline

def triangle(num):
    dp = [0] * (max(num,5)+1)
    # 초기값 설정
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2 # dp[1]+dp[3]
    dp[5] = 2 # dp[4]
    for n in range(6,num+1):
        dp[n]=dp[n-5]+dp[n-1]
    return dp[num]


t = int(input())
for _ in range(t):
    n = int(input())
    print(triangle(n))