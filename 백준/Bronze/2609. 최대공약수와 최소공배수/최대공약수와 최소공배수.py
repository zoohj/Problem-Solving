#2609 최대공약수와 최소공배수
'''
input: 자연수 2개
output: 최대 공약수(gcd), 최소 공배수(lcm)
최대공약수
최소공배수 = 두 수의 곱 / 최대공약수
'''

import sys
n, m= map(int, sys.stdin.readline().split())

def gcd(a, b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b%i==0:
            return i
        
def lcm(a,b,c):
    return a*b/c

g=gcd(n,m)
l=int(lcm(n,m,g))

print(g)
print(l)