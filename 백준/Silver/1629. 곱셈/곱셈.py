# https://www.acmicpc.net/problem/1629
# 1629 곱셈
# 알고리즘: 분할 정복
# 핵심: 어떻게하면 연산 개수를 줄일 수 있을지 생각

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

"""
우리가 구해야 하는 것
(a^b) % c

a를 b번 곱하면 시간 초과가 발생함.
=> '분할 정복' 사용.

<핵심 아이디어>

a^b
= (a^(b/2))^2  (b가 짝수일 때)

b가 홀수라면
a^b
= (a^(b//2))^2 * a

그리고 곱셈마다 %c 를 해도 결과는 동일.

(a * b) % c
= ((a % c) * (b % c)) % c

숫자가 커지기 전에 계속 %c 를 해줌.
"""

result = 1  # 최종 결과 저장

while b > 0:
    # b가 홀수라면
    # a를 결과에 한 번 곱해줘야 한다
    if b % 2 == 1:
        result = (result * a) % c

    # a를 제곱 (다음 단계 준비)
    # a^2, a^4, a^8 ... 이렇게 커짐
    a = (a * a) % c

    # b를 절반으로 줄임
    b = b // 2

print(result)
