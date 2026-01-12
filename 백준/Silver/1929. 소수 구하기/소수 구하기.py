#1929 소수 구하기
'''
M 이상 N 이하의 소수 모두 출력
'''

import math
import sys
input = sys.stdin.readline


m, n = map(int, input().split())

for target in range(m, n+1):
    if target < 2:
        continue
    is_prime = True
    sqr = int(math.sqrt(target))
    for i in range(2,sqr+1): #target까지 찾으면 시간초과 남
        # print("target:", target, "i:",i)
        if target%i==0:
            is_prime = False
            break

    if is_prime:
        print(target)