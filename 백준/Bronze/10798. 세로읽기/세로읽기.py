#10798 세로읽기
'''
5개의 단어
한줄에 최대 15자
'''

import sys
input = sys.stdin.readline

max_len = 0
words=[]
# 데이터 저장
for _ in range(5):
    word = input().rstrip()
    if len(word)>max_len:
        max_len = len(word)
    words.append(word)

for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end="")
print()