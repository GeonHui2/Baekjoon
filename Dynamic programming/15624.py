import sys

n = int(sys.stdin.readline())

a, b = 0, 1
for i in range(n):
    a, b = (a+b)%1000000007, a%1000000007
print(a)
