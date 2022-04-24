import sys
from math import factorial

n, k = map(int, sys.stdin.readline().split())

result = factorial(n) / (factorial(n - k) * factorial(k))

print(int(result))
