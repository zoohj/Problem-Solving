# https://www.acmicpc.net/problem/1316
# 1316 그룹 단어 체커

import sys

input = sys.stdin.readline
n = int(input())
count = 0
for _ in range(n):
    word = str(input().strip())
    com_word = [word[0]]
    for i in range(1, len(word)):
        if word[i] == com_word[-1]:
            continue
        com_word.append(word[i])

    # com_word에서 중복 문자 있는지 확인
    if len(com_word) == len(set(com_word)):
        count += 1

print(count)
