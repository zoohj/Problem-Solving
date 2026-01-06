#1259 팰린드롬수
'''
이효리
sees, 12421
무의미한 0 올 수 없음 (010)
input: 여러개의 테스트케이스(마지막줄 0)
output: yes / no

reversed() / [::-1]
'''

import sys


while True:
    c= sys.stdin.readline().strip()
    if c == '0':
        break

    if c==c[::-1]:
        print("yes")
    else:
        print("no")
