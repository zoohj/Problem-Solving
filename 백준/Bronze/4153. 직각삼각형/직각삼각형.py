#4153 직각삼각형
'''
input: A, B
ouput: 직각삼각형 확인(right, wrong)
'''

import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if sum(nums)==0:
        break

    nums.sort()

    if (nums[0]**2+nums[1]**2==nums[2]**2):
        print("right")
    else: 

        print("wrong")
