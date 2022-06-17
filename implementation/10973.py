import sys

n = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))

for i in range(n - 1, 0, -1):
    if result[i] < result[i - 1]:
        x, y = i - 1, i
        for j in range(n - 1, 0, -1):
            if result[j] < result[x]:
                result[j], result[x] = result[x], result[j]
                result = result[:i] + sorted(result[i:], reverse= True)
                print(*result)
                exit(0)
print(-1)
