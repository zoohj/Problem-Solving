# https://www.acmicpc.net/problem/1541
# 1541 잃어버린 괄호
# 알고리즘: 그리디(Greedy)
# 핵심: 뺄셈하는 수를 최대화


import sys
input = sys.stdin.readline

# '-'를 기준으로 문자열 분리
groups = list(map(str,input().split('-')))

dump = []
for group in groups:
    # 각 덩어리 내부의 '+' 기준으로 다시 분리
    numbers = map(int, group.split("+"))
    # 합을 구해 리스트에 저장
    dump.append(sum(numbers))

answer = dump[0]
for i in range(1, len(dump)):
    answer -= dump[i]

print(answer)