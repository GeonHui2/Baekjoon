import sys

n = int(sys.stdin.readline())
dp = [0] * 10001

for _ in range(n):
    dp[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(dp[i]):
        print(i)
