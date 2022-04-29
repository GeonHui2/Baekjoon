import sys

input = sys.stdin.readline

k = int(input())

result = []
for i in range(k):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        del result[-1]

print(sum(result))
