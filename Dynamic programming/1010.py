import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = n - m
    if n == m:
        print(1)
    else:
        print(int(math.factorial(m) / (math.factorial(m - n) * math.factorial(n))))
