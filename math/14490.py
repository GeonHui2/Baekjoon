import sys
import math

n, m = map(int, sys.stdin.readline().split(':'))

print(str(n // math.gcd(n, m)) + ":" + str(m // math.gcd(n, m)))
