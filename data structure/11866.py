import sys

input = sys.stdin.readline

n, k = map(int, input().split())

num = list(range(1, n + 1))

key = 0
temp = k - 1
result = []

while num:
    key = (key + temp) % len(num)
    result.append(num.pop(key))

print('<'+', '.join(map(str, result))+'>')
