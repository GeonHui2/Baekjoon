import sys

n = int(sys.stdin.readline())

dp = [0] * 91
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1): # 점화식을 이용해서 피보나치와 같은 원리로 수행한다.
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
