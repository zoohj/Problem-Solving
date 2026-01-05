#5597 과제 안 내신 분..?[배열]
'''
input: 출석번호 n을 한줄에 하나씩(중복 X)
ouput: 안 낸 학생 번호 (오름차순)
'''

import sys
lst = [num for num in range(1,31)]

for _ in range(28):
    lst.remove(int(sys.stdin.readline()))

for n in lst:
    print(n)