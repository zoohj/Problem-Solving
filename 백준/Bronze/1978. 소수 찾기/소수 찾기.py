#1978 소수 찾기
'''
input: 수의 개수 N, N개의 수
ouput: 주어진 수들 중 소수의 개수
'''

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count=0

# 1과 자기 자신만으로만 나누어 떨어짐 
for i in nums:
    if i == 1:
        pass

    else:
        for k in range(2, i):
            # print(f"i,k = {i},{k}")
            if (i%k==0):
                # print(f"i%k={i%k}")
                break
        else: 
            count += 1
            # print(f"count={count}")

print(count)