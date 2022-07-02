import sys
import math

n, k = map(int, sys.stdin.readline().split())

result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(result % 10007)
