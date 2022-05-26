import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(t):
    n = int(input())
    for i in range(4, n + 1): # 점화식을 이용하여 피보나치와 같은 원리로 계산한다.
        dp[i] = dp[i -2] + dp[i -3]
    print(dp[n])