#2798 블랙잭
'''
블랙잭 - 카드의 합을 21 넘지 않는 한도 내에서 최대한 크게
N장의 카드, 숫자 M
N장의 카드 중에서 3장 - M을 넘지 않으면서 최대한 가깝게
output: 3장의 합

nums[i]+nums[j]+nums[k] <= M

인덱스
i: 0~n-3
j: i~n-2
k: j~n-1
'''

import sys

n, m= map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))
result, total = 0, 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = nums[i]+nums[j]+nums[k]
            if total <= m and total > result:
                result = total

print(result)