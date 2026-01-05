#2292 벌집
'''
# 1, 7, 19, 37, 61
# 1, 6, 12, 18, 24
# 6씩 곱한 값만큼 
# 1~1 : 1
# 2~7 : 2
# 8~19: 3
# 20~37:4

# #b: before
# b+6*0, b+6*1, b+6*2, b+6*3

'''

import sys


n= int(sys.stdin.readline())
count=1
max_num=1
while n > max_num:
    max_num = max_num+6*count
    count += 1

print(count)