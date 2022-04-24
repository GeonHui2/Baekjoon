import sys

input = sys.stdin.readline

n = int(input())

result = []

for i in range(n):
    result.append(int(input()))

result.sort()

for i in range(n):
    print(result[i])
