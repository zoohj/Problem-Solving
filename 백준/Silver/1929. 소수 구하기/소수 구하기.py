#1929 소수 구하기
'''
M 이상 N 이하의 소수 모두 출력

방법 1. 제곱근까지만 확인
방법 2. 에라토스테네스의 체 = 소수의 배수들을 지워나가는 방식

'''

import math
import sys
input = sys.stdin.readline


m, n = map(int, input().split())



# 방법 2. 에라토스테네스의 체

'''
1. 2부터 N까지 목록
2. 지워지지 않은 가장 작은 수 p(맨 처음에는 2) 
3. p의 배수들을 목록에서 모두 지워
4. 다 지우면 (2 제외하고) 다음으로 작은수로 이동
5. N까지 반복하고 남은 숫자들이 모두 소수임

'''

# 그냥 prime_list[i]=(T/F)로 저장해서 접근하는게 빠름, 리스트에 숫자 넣지 않기!
prime_list = [True]*(n+1)
prime_list[0] = prime_list[1]=False

for i in range(2, int(math.sqrt(n)) +1):
    if prime_list[i]:
        for j in range(i*i, n+1, i):
            prime_list[j]= False

for i in range(m, n+1):
    if prime_list[i]:
        print(i)


# 방법 1. 제곱근까지 구현
# for target in range(m, n+1):
#     if target < 2:
#         continue
#     is_prime = True
#     sqr = int(math.sqrt(target))
#     for i in range(2,sqr+1): #target까지 찾으면 시간초과 남
#         # print("target:", target, "i:",i)
#         if target%i==0:
#             is_prime = False
#             break

#     if is_prime:
#         print(target)
