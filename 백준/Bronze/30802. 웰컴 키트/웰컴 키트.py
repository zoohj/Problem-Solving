#30802 웰컴 키트
'''
티셔츠 사이즈(6가지), T장 묶음 주문 (남아도 되지만 부족X)
펜(1종류), P자루 묶음 or 1자루 주문 (정확히 참가자 수만큼)
input: 
참가자 수 N, 
티셔츠 사이즈별 신청자 수 s, m, l, xl, xxl, xxxl
T, P
ouput: 티셔츠 최소 묶음 수, 펜 최대 묶음 수 및 한자루씩 몇 개
'''

import sys
import math

n = int(sys.stdin.readline())
t_size = list(map(int, sys.stdin.readline().split()))
t, p= map(int, sys.stdin.readline().split())

# t_bundle : 사이즈별로 t를 넘는 경우에, t_size[0]/t 하고 반올림(math.ceil())
t_bundle = 0 
for i in t_size:
    t_bundle += math.ceil(i/t)

p_bundle = n // p
p_count= n % p

print(t_bundle)
print(p_bundle, p_count, end=" ")
print()