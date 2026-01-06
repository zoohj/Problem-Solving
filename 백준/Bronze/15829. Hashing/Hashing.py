#15829 Hashing
'''
항의 번호에 해당하는 만큼 특정한 숫자 거듭제곱해서 곱해준 다음에 더함
abcde -> 12345 -> 1*31^0 + 2*31^1 + 3*31^2 + 4*31^3 + 5*31^4
1. 알파벳을 숫자로 바꾸고 (아스키코드변환 - 96)
2. 자리수(i)를 알아내서 31**i를 곱함
3. 다 더함
'''

import sys

n= int(sys.stdin.readline())
char_list= list(sys.stdin.readline().rstrip())
for i in range(n):
    char_list[i]=(ord(char_list[i])-96)*31**(i)
print(sum(char_list))
