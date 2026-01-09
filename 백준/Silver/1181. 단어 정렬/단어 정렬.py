#1181 단어 정렬
'''
input: 단어 개수 개수 n, n개의 단어
output: 단어의 길이가 짧은 것부터 긴 순으로 정렬(단, 중복된 단어 제거)
1. 단어가 같은게 있으면 삭제 => set 사용
2. 단어 길이 확인
3. 길이가 같으면 사전순 확인 (<) 

단어랑 길이랑 두개 다 있어야돼
'''

import sys
input = sys.stdin.readline
n = int(input()) # 개수

word_list=[]

for _ in range(n):
    word= input().strip()
    word_list.append((len(word),word))

# 중복 제거
word_list=list(set(word_list))
# 정렬
word_list.sort()

for word in word_list:
    print(word[1])