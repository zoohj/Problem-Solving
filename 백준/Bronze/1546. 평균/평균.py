#1546 평균
'''
최댓값
점수/M*100
'''

import sys
n= int(sys.stdin.readline())
score = list(map(float,sys.stdin.readline().split()))
max= max(score)
for i in range(n):
    score[i] = score[i]/max*100
print(sum(score)/n)