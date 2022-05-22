import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [1, 1, 2]

for i in range(3, n + 1):
    dp.append(dp[i - 1] * i)

print(dp[n] // (dp[m] * dp[n - m]))
