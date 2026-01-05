#2231 분해합
'''
N의 분해합: N과 N을 이루는 각 자리수의 합
M은 N의 생성자
ex)
256=245+2+4+5
245는 256의 생성자
'''

import sys

# 분해합 구하기
# 각 자리수 분해 -> N%10 -> //10 -> 소수점 아래 버려 -> N%10 반복 (N이 0일때까지)
# n= 245
# result = n
# while n!=0:
#     result += (n%10)
#     n=n//10
# print(result)

# 생성자 구하기 (brute force)
n = int(sys.stdin.readline())
for i in range(1, n+1):
    # print(i)
    result=i
    temp=i
    while temp > 0:
        result += temp%10
        temp=temp//10
    if result==n:
        print(i)
        break
else:
    print(0) # 생성자 없음
        