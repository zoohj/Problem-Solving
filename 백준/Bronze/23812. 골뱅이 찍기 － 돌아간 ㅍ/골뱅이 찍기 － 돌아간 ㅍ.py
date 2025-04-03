N= int(input())

def solve(n):
  for _ in range(n):
    print('@'*n + ' '*(3*n) + '@'*n)

  for _ in range(n):
    print('@'*(5*n))

  for _ in range(n):
    print('@'*n + ' '*(3*n) + '@'*n)

  for _ in range(n):
    print('@' * (5 * n))

  for _ in range(n):
    print('@' * n + ' ' * (3 * n) + '@' * n)

solve(N)