#9095 1, 2, 3 더하기
'''
n을 1,2,3의 합으로 나타내는 방법의 수
<1>
1
<2>
11 2
<3>
111 21 / 12 3
<4>
1111 211 121 31 / 112 22 / 13
<5>
11111 2111 1211 311 1121 221 131 / 1112 212 122 32 / 113 23
'''

import sys
input = sys.stdin.readline

# t = int(input()) # 테스트 케이스
# n = int(input()) 

import sys
input = sys.stdin.readline

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

# n이 11로 적기때문에 미리 배열 만들어놓음
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
