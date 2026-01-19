#11726 2xn 타일링
'''
2xn 크기 직사각형 채우는 방법 수
'''

import sys
input = sys.stdin.readline


n = int(input())

"""
n
1 1
2 11 =
3 111 1= =1 
4 1111 =11 1=1 11= == 
5 11111 -111 1-11 11-1 111- 1-- -1- --1 

dp[] 
"""
# dp 테이블 초기화
dp=[0]*1001

dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2]) % 10007

print(dp[n])