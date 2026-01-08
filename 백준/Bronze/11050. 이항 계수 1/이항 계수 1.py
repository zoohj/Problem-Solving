#11050 이항 계수
'''
input: 자연수 N, 정수 K
ouput: 이항 계수(N개 중에서 K개를 순서 없이 뽑는 방법의 수)
n! / k!(n-k)!
'''


import math
import sys
input = sys.stdin.readline
fac= math.factorial

n, k = map(int,input().split())

result = fac(n)/(fac(k)*fac(n-k))
print(int(result))