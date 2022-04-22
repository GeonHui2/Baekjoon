import sys
input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    result.append(int(input()))

cnt = 1
result.sort(reverse=True)
for j in range(n):
    result[j] = result[j] * cnt
    cnt += 1


print(max(result))
