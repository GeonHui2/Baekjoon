import sys

input = sys.stdin.readline

n = int(input())

a, b = 1, 2

for i in range(1, n):
    a, b = b, (a + b) % 10

print(a)
