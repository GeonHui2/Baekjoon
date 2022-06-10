import sys

n = int(sys.stdin.readline())

power = [0] * 10001

for i in range(1, n + 1):
    power[i] = int(sys.stdin.readline())

dp = [0] * 10001
dp[1] = power[1]
dp[2] = power[1] + power[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + power[i - 1] + power[i], dp[i - 2] + power[i])

print(dp[n])
