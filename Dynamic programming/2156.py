import sys

n = int(sys.stdin.readline())

power = []
for _ in range(n):
    power.append(int(sys.stdin.readline()))

dp = [0] * (n + 1)
dp[1] = power[0]
dp[2] = power[0] + power[1]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 3] + power[i - 2] + power[i - 1], dp[i - 2] + power[i  -1])

print(dp[n])
